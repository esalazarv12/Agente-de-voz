# 🧩 Anatomía de la Complejidad

# 📘 Evaluación Arquitectónica Basada en “A Philosophy of Software Design”

Siguiendo los conceptos propuestos por John Ousterhout, se realizó un análisis del sistema identificando módulos profundos (Deep Modules), módulos superficiales (Shallow Modules) y posibles fugas de información (Information Leakage).

---

# 🧠 Módulos Profundos (Deep Modules)

Según Ousterhout, un módulo profundo es aquel que ofrece una interfaz simple mientras encapsula una gran cantidad de complejidad interna.

En el proyecto, los mejores ejemplos de módulos profundos fueron:

---

## 🎤 audio_input.py

### Interfaz expuesta

```python
await capture_audio(audio_queue)
```

### Complejidad ocultada

Este módulo encapsula:

* Captura de audio en tiempo real
* Integración con dispositivos de entrada
* Comunicación async
* Conversión de buffers de audio
* Integración con sounddevice
* Gestión del loop concurrente

Toda esta complejidad queda escondida detrás de una interfaz extremadamente pequeña y clara.

---

## 🧠 stt.py

### Interfaz expuesta

```python
await speech_to_text(audio_queue, text_queue)
```

### Complejidad ocultada

Este módulo abstrae:

* Conversión de audio temporal
* Procesamiento con Whisper
* Integración con FFmpeg
* Transcripción offline
* Manejo de colas async

El resto del sistema nunca necesita conocer cómo funciona Whisper internamente.

---

## 🤖 llm.py

### Interfaz expuesta

```python
await generate_response(text_queue, response_queue)
```

### Complejidad ocultada

El módulo encapsula:

* Comunicación con Ollama
* Gestión de prompts
* Integración con llama3
* Procesamiento de respuestas
* Flujo conversacional

La interfaz permanece simple mientras la lógica interna puede evolucionar independientemente.

---

# ⚠️ Módulos Superficiales (Shallow Modules)

Durante el desarrollo se identificaron intentos iniciales de dividir excesivamente el sistema en archivos muy pequeños con poca responsabilidad real.

Esto generaba:

* Demasiadas llamadas entre módulos
* Complejidad accidental
* Navegación difícil
* Acoplamiento innecesario

Siguiendo los principios de Ousterhout, se decidió evitar atomizar artificialmente el sistema.

En lugar de crear múltiples capas vacías, se consolidó la lógica relacionada en módulos más amplios y profundos.

---

# 🔍 Ejemplo de Corrección

Inicialmente se consideró separar:

* manejo de buffers
* conversión WAV
* integración Whisper
* limpieza temporal

en distintos archivos.

Sin embargo, esto habría producido módulos superficiales con poca capacidad real de ocultamiento.

Finalmente toda esa lógica se consolidó dentro de `stt.py`, aumentando la profundidad del módulo.

---

# 🔐 Information Leakage (Fuga de Información)

Uno de los riesgos arquitectónicos detectados fue la posibilidad de que detalles internos de implementación se filtraran hacia otros módulos.

---

## ⚠️ Riesgo Detectado

Detalles como:

* formato interno del audio
* configuración de Whisper
* llamadas específicas a Ollama
* dependencias de FFmpeg

podían propagarse a múltiples partes del sistema.

Esto habría aumentado el acoplamiento y dificultado futuras modificaciones.

---

# ✅ Solución Aplicada

Se aplicó ocultamiento de información mediante:

* Interfaces mínimas
* Uso de asyncio.Queue
* Encapsulamiento por responsabilidades
* Separación estricta entre módulos

Gracias a esto:

* El pipeline no depende de implementaciones concretas
* Whisper podría reemplazarse sin modificar el resto del sistema
* El LLM podría cambiarse fácilmente
* La arquitectura mantiene elasticidad frente al cambio

---

# 🚀 Conclusión

El análisis arquitectónico demostró que la profundidad modular fue uno de los principales factores que permitió mantener la simplicidad del sistema a pesar de integrar múltiples tecnologías complejas.

La reducción de fuga de información y la consolidación de módulos profundos ayudaron a disminuir complejidad accidental y mejorar mantenibilidad.
