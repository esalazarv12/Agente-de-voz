# 🎤 Software Journey — Agente de Voz Conversacional

## 📌 Descripción General

Este repositorio documenta el proceso completo de diseño, construcción y evaluación arquitectónica de un agente conversacional de voz desarrollado con Python puro y programación asíncrona utilizando `asyncio`.

El proyecto implementa el pipeline:

```text
Micrófono → Speech-to-Text → LLM → Text-to-Speech → Altavoz
```

La documentación se centra en analizar críticamente la colaboración hombre-máquina durante el desarrollo, aplicando conceptos de ingeniería de software moderna inspirados en el libro:

> "A Philosophy of Software Design" — John Ousterhout

---

# 📚 Índice del Software Journey

## 1️⃣ La Bala Trazadora y el Enrutamiento de Skills

Análisis del riesgo inicial, estrategia de exploración y decisiones tempranas de arquitectura.

➡ Ver documento:
[tracer-bullet.md](./tracer-bullet.md)

---

## 2️⃣ Anatomía de la Complejidad

Evaluación de módulos profundos, módulos superficiales y control de fuga de información.

➡ Ver documento:
[complexity-analysis.md](./complexity-analysis.md)

---

## 3️⃣ Veredicto Retrospectivo de los Sub-Agentes

Análisis retrospectivo del checkpoint arquitectónico y elasticidad del sistema frente al cambio.

➡ Ver documento:
[retrospective.md](./retrospective.md)

---

# 🧠 Tecnologías Utilizadas

* Python
* asyncio
* Whisper
* Ollama
* llama3
* pyttsx3
* sounddevice
* NumPy

---

# 🎯 Objetivo del Proyecto

Comprender profundamente la arquitectura detrás de frameworks modernos de agentes conversacionales en tiempo real mediante una implementación manual y modular basada en programación asíncrona.
