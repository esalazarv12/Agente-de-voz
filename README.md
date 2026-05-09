<<<<<<< HEAD
# 🎤 Agente de Voz Conversacional con Python y asyncio

Proyecto desarrollado en Python puro utilizando `asyncio` para comprender la arquitectura interna detrás de frameworks modernos de agentes conversacionales en tiempo real como Pipecat y LiveKit Agents.

El sistema implementa un pipeline conversacional completo en tiempo real:

```text
Micrófono → Speech-to-Text → LLM → Text-to-Speech → Altavoz
```

Todo el procesamiento se ejecuta localmente utilizando modelos y herramientas offline.

---

# 🚀 Características del Proyecto

- Captura de audio en tiempo real desde el micrófono
- Conversión de voz a texto usando Whisper local
- Generación de respuestas mediante un LLM local con Ollama
- Conversión de texto a voz usando pyttsx3
- Arquitectura asíncrona utilizando `asyncio`
- Comunicación entre módulos mediante `asyncio.Queue`
- Pipeline modular y concurrente
- Ejecución completamente local y offline

---

# 🧠 Aplicación del flujo “Running Your AFK Agent”

Este proyecto implementa los principios del flujo de trabajo “Running Your AFK Agent”, construyendo manualmente un agente conversacional en tiempo real utilizando Python puro y programación asíncrona.

Cada componente del sistema se ejecuta concurrentemente y se comunica mediante colas asíncronas (`asyncio.Queue`), simulando el comportamiento interno de frameworks profesionales de agentes de voz.

Flujo implementado:

```text
capture_audio()
        ↓
audio_queue
        ↓
speech_to_text()
        ↓
text_queue
        ↓
generate_response()
        ↓
response_queue
        ↓
text_to_speech()
```

El sistema permanece en ejecución continua escuchando audio, procesando transcripciones, generando respuestas y reproduciendo voz sintetizada.

---

# 🏗️ Arquitectura del Proyecto

## Backend

El backend del proyecto se encarga de:

- Captura de audio
- Procesamiento de voz
- Transcripción de audio
- Comunicación con el LLM
- Generación de respuestas
- Conversión texto a voz
- Orquestación asíncrona

Tecnologías utilizadas:

- Python
- asyncio
- Whisper
- Ollama
- llama3
- pyttsx3

---

## Frontend

El frontend se implementa mediante una interfaz de línea de comandos (CLI) en tiempo real.

La consola muestra:

- Estado del micrófono
- Estado de transcripción
- Estado del modelo de IA
- Respuestas generadas
- Estado de reproducción de voz

---

# 📁 Estructura del Proyecto

```text
Agente-de-voz/
│
├── app/
│   ├── main.py
│   ├── audio_input.py
│   ├── stt.py
│   ├── llm.py
│   ├── tts.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Instalación del Proyecto

## 1. Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
```

---

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 3. Instalar FFmpeg

Whisper requiere FFmpeg para procesar audio.

Descargar desde:

https://www.gyan.dev/ffmpeg/builds/

Agregar `ffmpeg/bin` al PATH del sistema.

---

## 4. Instalar Ollama

Descargar Ollama desde:

https://ollama.com/

---

## 5. Descargar el modelo llama3

```bash
ollama pull llama3
```

---

# ▶️ Ejecución del Proyecto

```bash
python -m app.main
```

---

# 💬 Ejemplo de Funcionamiento

```text
[🎤 Escuchando...]
[📝 Texto]: hola
[🧠 Pensando...]
[🤖 Respuesta]: Hola, ¿cómo estás?
[🔊 Hablando...]
```

---

# 🔄 Diseño Asíncrono

El proyecto utiliza `asyncio.gather()` para ejecutar múltiples tareas concurrentes:

- Captura de audio
- Speech-to-Text
- Generación de respuestas
- Text-to-Speech

Cada módulo funciona de manera independiente y se comunica utilizando colas asíncronas, permitiendo un flujo continuo en tiempo real.

---

# 📦 Tecnologías Utilizadas

- Python 3
- asyncio
- sounddevice
- soundfile
- NumPy
- Whisper
- Ollama
- llama3
- pyttsx3
- FFmpeg

---

# 🔮 Posibles Mejoras Futuras

- Voice Activity Detection (VAD)
- Streaming de audio en tiempo real
- Cancelación de eco
- Interfaz gráfica
- Activación por palabra clave
- Memoria conversacional
- Comunicación mediante WebSockets
- Dockerización del proyecto

---

# 👨‍💻 Autor

Proyecto desarrollado con fines educativos para comprender la arquitectura de agentes conversacionales de voz en tiempo real utilizando Python puro y programación asíncrona.
=======
# 🎤 Agente de Voz Conversacional con Python y asyncio

Proyecto desarrollado en Python puro utilizando `asyncio` para comprender la arquitectura interna detrás de frameworks modernos de agentes conversacionales en tiempo real como Pipecat y LiveKit Agents.

El sistema implementa un pipeline conversacional completo en tiempo real:

```text
Micrófono → Speech-to-Text → LLM → Text-to-Speech → Altavoz
```

Todo el procesamiento se ejecuta localmente utilizando modelos y herramientas offline.

---

# 🚀 Características del Proyecto

- Captura de audio en tiempo real desde el micrófono
- Conversión de voz a texto usando Whisper local
- Generación de respuestas mediante un LLM local con Ollama
- Conversión de texto a voz usando pyttsx3
- Arquitectura asíncrona utilizando `asyncio`
- Comunicación entre módulos mediante `asyncio.Queue`
- Pipeline modular y concurrente
- Ejecución completamente local y offline

---

# 🧠 Aplicación del flujo “Running Your AFK Agent”

Este proyecto implementa los principios del flujo de trabajo “Running Your AFK Agent”, construyendo manualmente un agente conversacional en tiempo real utilizando Python puro y programación asíncrona.

Cada componente del sistema se ejecuta concurrentemente y se comunica mediante colas asíncronas (`asyncio.Queue`), simulando el comportamiento interno de frameworks profesionales de agentes de voz.

Flujo implementado:

```text
capture_audio()
        ↓
audio_queue
        ↓
speech_to_text()
        ↓
text_queue
        ↓
generate_response()
        ↓
response_queue
        ↓
text_to_speech()
```

El sistema permanece en ejecución continua escuchando audio, procesando transcripciones, generando respuestas y reproduciendo voz sintetizada.

---

# 🏗️ Arquitectura del Proyecto

## Backend

El backend del proyecto se encarga de:

- Captura de audio
- Procesamiento de voz
- Transcripción de audio
- Comunicación con el LLM
- Generación de respuestas
- Conversión texto a voz
- Orquestación asíncrona

Tecnologías utilizadas:

- Python
- asyncio
- Whisper
- Ollama
- llama3
- pyttsx3

---

## Frontend

El frontend se implementa mediante una interfaz de línea de comandos (CLI) en tiempo real.

La consola muestra:

- Estado del micrófono
- Estado de transcripción
- Estado del modelo de IA
- Respuestas generadas
- Estado de reproducción de voz

---

# 📁 Estructura del Proyecto

```text
Agente-de-voz/
│
├── app/
│   ├── main.py
│   ├── audio_input.py
│   ├── stt.py
│   ├── llm.py
│   ├── tts.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Instalación del Proyecto

## 1. Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
```

---

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 3. Instalar FFmpeg

Whisper requiere FFmpeg para procesar audio.

Descargar desde:

https://www.gyan.dev/ffmpeg/builds/

Agregar `ffmpeg/bin` al PATH del sistema.

---

## 4. Instalar Ollama

Descargar Ollama desde:

https://ollama.com/

---

## 5. Descargar el modelo llama3

```bash
ollama pull llama3
```

---

# ▶️ Ejecución del Proyecto

```bash
python -m app.main
```

---

# 💬 Ejemplo de Funcionamiento

```text
[🎤 Escuchando...]
[📝 Texto]: hola
[🧠 Pensando...]
[🤖 Respuesta]: Hola, ¿cómo estás?
[🔊 Hablando...]
```

---

# 🔄 Diseño Asíncrono

El proyecto utiliza `asyncio.gather()` para ejecutar múltiples tareas concurrentes:

- Captura de audio
- Speech-to-Text
- Generación de respuestas
- Text-to-Speech

Cada módulo funciona de manera independiente y se comunica utilizando colas asíncronas, permitiendo un flujo continuo en tiempo real.

---

# 📦 Tecnologías Utilizadas

- Python 3
- asyncio
- sounddevice
- soundfile
- NumPy
- Whisper
- Ollama
- llama3
- pyttsx3
- FFmpeg

---

# 🔮 Posibles Mejoras Futuras

- Voice Activity Detection (VAD)
- Streaming de audio en tiempo real
- Cancelación de eco
- Interfaz gráfica
- Activación por palabra clave
- Memoria conversacional
- Comunicación mediante WebSockets
- Dockerización del proyecto

---

# 👨‍💻 Autor

Proyecto desarrollado con fines educativos para comprender la arquitectura de agentes conversacionales de voz en tiempo real utilizando Python puro y programación asíncrona.
>>>>>>> 6666a040a3638b836004ae20abb7d9327ff00934
