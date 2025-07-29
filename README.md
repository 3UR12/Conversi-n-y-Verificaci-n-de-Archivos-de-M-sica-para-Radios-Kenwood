# 📁 README.md — Conversión y Verificación de Archivos de Música para Radios Kenwood

---

## 🎯 Objetivo

Este proyecto contiene tres scripts útiles para garantizar la compatibilidad de archivos de música con radios de auto Kenwood:

1. `convertir_a_mp3.py`: Convierte múltiples archivos de audio (m4a, aac, wav, etc.) a MP3 compatibles (44.1 kHz, 128/192 kbps, estéreo, CBR).
2. `verificar_mp3.py`: Analiza los archivos `.mp3` en una carpeta y detecta si son compatibles con los parámetros comunes de radios de auto.
3. `analizar_audio.py`: Muestra información detallada de cualquier archivo de audio para ayudarte a diagnosticar problemas de compatibilidad.

---

## ✅ Requisitos

### 🐍 1. Python

Debes tener instalado Python 3.8 o superior. Verifica con:

```bash
python --version
```

---

### 📦 2. Instalación de dependencias Python

Instala las librerías necesarias con el siguiente comando:

```bash
pip install moviepy pymediainfo
```

---

### ⚙️ 3. Instalación opcional de FFmpeg (recomendado para conversión)

Para que el script de conversión funcione correctamente, es **altamente recomendable** instalar FFmpeg, una herramienta de línea de comandos para procesamiento multimedia.

* Puedes descargar FFmpeg para tu sistema operativo aquí:

  * Windows: [https://ffmpeg.org/download.html#build-windows](https://ffmpeg.org/download.html#build-windows)
  * Linux: [https://ffmpeg.org/download.html#build-linux](https://ffmpeg.org/download.html#build-linux)
  * macOS: [https://ffmpeg.org/download.html#build-mac](https://ffmpeg.org/download.html#build-mac)

* En Windows, después de descargarlo, extrae la carpeta y agrega la ruta a `bin` a la variable de entorno `PATH` para poder usarlo desde la terminal.

* Verifica que FFmpeg esté instalado correctamente ejecutando:

```bash
ffmpeg -version
```

> **Nota:** Si no instalas FFmpeg, el script de conversión no podrá funcionar, pero los otros scripts (verificación y análisis) sí.

---

## 🛠️ Uso de los scripts

---

### 📌 Script 1: `convertir_a_mp3.py`

Este script convierte en lote todos los archivos de audio en una carpeta (y subcarpetas) a **MP3 compatible con radios Kenwood**.

#### 🎵 Parámetros de salida recomendados:

* Formato: `.mp3`
* Bitrate: 128k o 192k **CBR** (no VBR)
* Sample Rate: 44100 Hz
* Canales: 2 (estéreo)
* Sin metadatos ni portadas (opcional)

### 📁 Configura tu carpeta

Edita el script para indicar la carpeta origen y destino, y ajusta parámetros si deseas:

```python
CARPETA_ORIGEN = r"D:\Music mor"     # Carpeta donde están tus archivos originales
CARPETA_DESTINO = r"D:\Music_MP3"    # Carpeta donde se guardarán los archivos convertidos
BITRATE = "192k"                     # Puedes usar "128k" si lo prefieres
NORMALIZAR_NOMBRES = True            # Elimina acentos y caracteres raros
STRIP_METADATA = True                # Elimina metadatos y portadas
```

---

### ▶️ Ejecutar el script

Desde la terminal, dentro de la carpeta donde esté el script, ejecuta:

```bash
python convertir_a_mp3.py
```

✅ El script recorrerá todas las carpetas dentro de `CARPETA_ORIGEN` y guardará los nuevos MP3 en `CARPETA_DESTINO`.

---

### 🔍 Script 2: `verificar_mp3.py`

Este script revisa los archivos `.mp3` en una carpeta y lista aquellos que **NO cumplen** con los requisitos mínimos para ser compatibles con radios de auto Kenwood.

### 📁 Configura tu carpeta

Edita esta línea en el script para la ruta a verificar:

```python
CARPETA = r"D:\Music_MP3"
```

---

### ▶️ Ejecutar el script

```bash
python verificar_mp3.py
```

El script mostrará un resumen con los archivos potencialmente problemáticos.

---

### 🔎 Script 3 (Extra): `analizar_audio.py`

Este script muestra información detallada de cualquier archivo de audio, útil para diagnosticar problemas de compatibilidad.

---

### 🛠 Requisitos para este script

* Python 3.x
* La librería `pymediainfo` (instalada previamente con `pip install pymediainfo`)
* **MediaInfo** debe estar instalado en tu sistema ([https://mediaarea.net/en/MediaInfo](https://mediaarea.net/en/MediaInfo)) para que `pymediainfo` funcione correctamente.

---

### 📜 Código completo (`analizar_audio.py`)

```python
from pymediainfo import MediaInfo

def analizar_audio(ruta_archivo):
    media_info = MediaInfo.parse(ruta_archivo)
    for track in media_info.tracks:
        if track.track_type == 'Audio':
            print(f"Archivo: {ruta_archivo}")
            print(f"Codec: {track.codec}")
            print(f"Bitrate: {track.bit_rate} bps")
            print(f"Sample rate: {track.sampling_rate} Hz")
            print(f"Canales: {track.channel_s}")
            print(f"Duración: {track.duration / 1000:.2f} segundos")
            print(f"Formato: {track.format}")
            print("-" * 40)

# Ejemplo de uso
if __name__ == "__main__":
    analizar_audio(r"D:\relax\stivijoes-- Cómo Sienta Ser de Hielo.mp3")
```

---

## 📌 Recomendaciones para radios Kenwood

* Usa una USB formateada en **FAT32**
* Usa archivos `.mp3` en **CBR**, 44.1 kHz, 128–192 kbps
* Evita nombres con acentos, emojis, o símbolos especiales
* No uses carpetas anidadas en exceso
* Expulsa siempre la USB de forma segura para evitar corrupción

---

## 🧪 Prueba rápida

Coloca solo uno o dos archivos `.mp3` convertidos en la raíz del USB y verifica si tu radio los reconoce. Si funcionan, puedes cargar el resto.

---

## 🙌 Créditos

* Código desarrollado por \[3UR12]
* Basado en herramientas y librerías open source:

  * [FFmpeg](https://ffmpeg.org/) para la conversión de audio
  * [MoviePy](https://zulko.github.io/moviepy/) para manipulación multimedia en Python
  * [pymediainfo](https://github.com/lieuwegeerts/pymediainfo) para análisis de archivos de audio
* Gracias a la comunidad de desarrolladores por estas herramientas libres.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.
