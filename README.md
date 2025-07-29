### 📁 `README.md` — Conversión y Verificación de Archivos de Música para Radios Kenwood

---

## 🎯 Objetivo

Este proyecto contiene dos scripts útiles para garantizar la compatibilidad de archivos de música con radios de auto Kenwood:

1. `convertir_a_mp3.py`: Convierte múltiples archivos de audio (m4a, aac, wav, etc.) a MP3 compatibles (44.1 kHz, 128/192 kbps, estéreo, CBR).
2. `verificar_mp3.py`: Analiza los archivos `.mp3` en una carpeta y detecta si son compatibles con los parámetros comunes de radios de auto.

---

## ✅ Requisitos

### 🐍 1. Python

Debes tener instalado Python 3.8 o superior. Verifica con:

```bash
python --version
```

---

### 📦 2. Instalación de dependencias

#### a. Instala `moviepy` (para conversión):

```bash
pip install moviepy
```

#### b. Instala `pymediainfo` (para verificación):

```bash
pip install pymediainfo
```

#### c. Instala `FFmpeg` (fundamental para la conversión):

* Descarga desde: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
* En Windows: extrae y agrega la carpeta `bin` a las **variables de entorno del sistema** (PATH).
* Verifica con:

```bash
ffmpeg -version
```

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

Edita el script en las siguientes líneas:

```python
CARPETA_ORIGEN = r"D:\Music mor"     # Carpeta donde están tus archivos originales
CARPETA_DESTINO = r"D:\Music_MP3"    # Carpeta donde se guardarán los archivos convertidos
BITRATE = "192k"                     # Puedes usar "128k" si lo prefieres
```

Opcional:

```python
NORMALIZAR_NOMBRES = True            # Elimina acentos y caracteres raros
STRIP_METADATA = True                # Elimina metadatos y portadas
```

---

### ▶️ Ejecutar el script

Abre la terminal y ejecuta:

```bash
python convertir_a_mp3.py
```

✅ El script recorrerá todas las carpetas dentro de `CARPETA_ORIGEN` y guardará los nuevos MP3 en `CARPETA_DESTINO`.

---

## 🔍 Script 2: `verificar_mp3.py`

Este script revisa los archivos `.mp3` en una carpeta y lista los que **NO cumplen** con los requisitos de compatibilidad.

### 📁 Configura tu carpeta

Edita esta línea en el script:

```python
CARPETA = r"D:\Music_MP3"
```

---

### ▶️ Ejecutar el script

```bash
python verificar_mp3.py
```

📋 Mostrará un resumen de los archivos que pueden causar problemas en tu radio.

---

## 📌 Recomendaciones para radios Kenwood

* Usa una USB formateada en **FAT32**
* Usa archivos `.mp3` en **CBR**, 44.1 kHz, 128–192 kbps
* Evita nombres con acentos, emojis, o símbolos raros
* No uses carpetas anidadas excesivamente
* Expulsa siempre la USB de forma segura

---

## 🧪 Prueba rápida

Coloca solo uno o dos archivos `.mp3` generados en la raíz del USB para probar si tu radio los reconoce. Si funcionan, puedes cargar el resto.



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

---
