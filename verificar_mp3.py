from pymediainfo import MediaInfo
from pathlib import Path

CARPETA = r"D:\Music_MP3"  # carpeta a verificar

def es_compatible(ruta: Path) -> bool:
    mi = MediaInfo.parse(str(ruta))
    for t in mi.tracks:
        if t.track_type == "Audio":
            formato = (t.format or "").lower()
            sr = int(t.sampling_rate or 0)
            ch = int(t.channel_s or 0)
            br = int(t.bit_rate or 0)
            # Reglas mínimas para Kenwood
            if "mpeg audio" in formato or "mp3" in formato:
                if sr == 44100 and ch <= 2 and (96000 <= br <= 320000):
                    return True
    return False

def revisar():
    malos = []
    for p in Path(CARPETA).rglob("*"):
        if p.is_file() and p.suffix.lower() == ".mp3":
            if not es_compatible(p):
                malos.append(p)
    if malos:
        print("Archivos potencialmente NO compatibles:")
        for m in malos:
            print(" -", m)
    else:
        print("Todo parece compatible según las reglas básicas.")

if __name__ == "__main__":
    revisar()
