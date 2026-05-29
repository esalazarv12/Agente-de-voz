# 🧩 architecture-checkpoint.md

# Mid-Sprint Architecture Review

## 📌 Diagnóstico Inicial

El sistema implementa correctamente un pipeline conversacional en tiempo real utilizando módulos desacoplados y programación asíncrona. Sin embargo, se identificaron oportunidades de mejora relacionadas con:

* Acoplamiento implícito entre audio input y TTS
* Loops infinitos sin control de estado
* Falta de filtrado de silencios
* Escalabilidad limitada del pipeline

---

# 🔍 Oportunidades de profundización (Deepening Opportunities)

## 1. Sistema de control de estados

Permitir que el agente controle cuándo escuchar y cuándo hablar.

## 2. Pipeline orientado a eventos

Reemplazar loops continuos por activación mediante eventos.

## 3. Voice Activity Detection (VAD)

Evitar procesamiento innecesario de silencios.

---

# 🧠 Simulación Multi-Agente Paralela

## 🤖 Sub-agente A — State Manager Centralizado

### Propuesta

Crear un módulo centralizado que controle estados:

* LISTENING
* THINKING
* SPEAKING

### Ventajas

* Evita feedback de audio
* Mejor control del flujo

### Desventajas

* Mayor complejidad de coordinación

---

## 🤖 Sub-agente B — Arquitectura Event-Driven

### Propuesta

Transformar el pipeline a eventos asincrónicos activados por triggers.

### Ventajas

* Mayor escalabilidad
* Mejor desacoplamiento

### Desventajas

* Requiere reestructuración completa

---

## 🤖 Sub-agente C — Integración VAD

### Propuesta

Implementar Voice Activity Detection antes del STT.

### Ventajas

* Reduce consumo
* Mejora precisión
* Evita silencios

### Desventajas

* Requiere calibración de audio

---

# ✅ Solución Híbrida Seleccionada

Se decidió combinar:

* State Manager
* Voice Activity Detection

La arquitectura event-driven completa se pospone para futuras iteraciones debido al costo de refactorización.

---

# 🚀 Resultado Esperado

Con esta mejora:

* Se reducirá ruido del pipeline
* Mejorará la experiencia conversacional
* Se reducirá procesamiento innecesario
* Se preparará el sistema para futuras extensiones
