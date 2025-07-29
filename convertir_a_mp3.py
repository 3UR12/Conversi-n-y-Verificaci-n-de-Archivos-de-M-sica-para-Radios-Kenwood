import os
import subprocess
import unicodedata
from pathlib import Path

# === CONFIGURA AQUÍ ===
CARPETA_ORIGEN = r"D:\Music mor"   # carpeta con tu música
CARPETA_DESTINO = r"D:\Music_MP3"  # a dónde guardar los MP3 convertidos
BITRATE = "192k"                   # 128k o 192k recomendados
NORMALIZAR_NOMBRES = True          # True para quitar acentos/caracteres raros
STRIP_METADATA = True              # True para quitar metadatos/portadas (recomendado)
REENCODAR_MP3_EXISTENTES = False   # True si quieres forzar CBR 192k a MP3 ya existentes

EXTS_ENTRADA = {".m4a", ".aac", ".wav", ".flac", ".ogg", ".wma", ".mp3"}  # .mp3 opcional

def nombre_ascii_seguro(nombre: str) -> str:
    # elimina acentos y caracteres problemáticos
    nfkd = unicodedata.normalize("NFKD", nombre)
    ascii_str = "".join(c for c in nfkd if not unicodedata.combining(c))
    # quita caracteres que a veces molestan a radios
    ascii_str = "".join(c if c.isalnum() or c in " .-_()" else "_" for c in ascii_str)
    return ascii_str

def convertir_a_mp3_ffmpeg(src: Path, dst: Path) -> bool:
    dst.parent.mkdir(parents=True, exist_ok=True)
    # Construimos comando FFmpeg para CBR + 44.1kHz + 2ch + ID3v2.3
    cmd = [
        "ffmpeg", "-y",
        "-i", str(src),
        "-vn",                      # sin video/portadas
        "-c:a", "libmp3lame",
        "-ar", "44100",
        "-ac", "2",
        "-b:a", BITRATE,
        "-maxrate", BITRATE,        # fuerza CBR
        "-minrate", BITRATE,
        "-bufsize", "64k",
        "-id3v2_version", "3",
        "-write_id3v1", "1",
    ]
    if STRIP_METADATA:
        cmd += ["-map_metadata", "-1"]  # quita metadatos (incluye portada)
    cmd += [str(dst)]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(f"✔ Convertido: {src} -> {dst}")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Error al convertir: {src}")
        return False

def procesar():
    for root, _, files in os.walk(CARPETA_ORIGEN):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTS_ENTRADA:
                src = Path(root) / f
                rel = src.relative_to(CARPETA_ORIGEN)
                nombre_sin_ext = rel.stem
                if NORMALIZAR_NOMBRES:
                    nombre_sin_ext = nombre_ascii_seguro(nombre_sin_ext)
                dst_rel = rel.with_name(nombre_sin_ext).with_suffix(".mp3")
                dst = Path(CARPETA_DESTINO) / dst_rel

                # Si es MP3 y no quieres re-encodar, solo copia (o sáltalo)
                if ext == ".mp3" and not REENCODAR_MP3_EXISTENTES:
                    if not dst.exists():
                        dst.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            with open(src, "rb") as i, open(dst, "wb") as o:
                                o.write(i.read())
                            print(f"= Copiado (mp3 ya compatible): {src} -> {dst}")
                        except Exception as e:
                            print(f"❌ Error al copiar {src}: {e}")
                    continue

                convertir_a_mp3_ffmpeg(src, dst)

if __name__ == "__main__":
    procesar()
