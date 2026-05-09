Nombre del proyecto:
Voice Agent Async (nombre provisional)

Objetivo:
Desarrollar un agente de voz conversacional en tiempo real usando Python puro y asyncio, que permita mantener una conversación fluida mediante el siguiente flujo:

Micrófono → Speech-to-Text → LLM → Text-to-Speech → Altavoz

Problema que resuelve:
La mayoría de frameworks modernos como Pipecat o LiveKit abstraen demasiado la lógica interna de los agentes de voz. Este proyecto busca entender desde cero cómo funciona esa arquitectura.

Solución propuesta:
Construir un sistema modular que capture audio desde el micrófono, lo transcriba a texto, lo procese con un modelo de lenguaje y devuelva una respuesta en audio reproducida en tiempo real.

Alcance (Scope):

Captura de audio desde micrófono
Transcripción (Speech-to-Text)
Procesamiento con LLM
Generación de voz (Text-to-Speech)
Reproducción por altavoces
Loop conversacional continuo
Arquitectura asíncrona con asyncio

Componentes del sistema:

Backend:

Orquestación del flujo con asyncio
Integración con APIs (STT, LLM, TTS)
Manejo de eventos en tiempo real

Frontend (mínimo pero válido):

Interfaz en consola (CLI interactivo)
Indicadores de estado (escuchando, pensando, respondiendo)

Nivel de complejidad:

Manejo de concurrencia
Streaming de datos
Integración de múltiples servicios
Pipeline en tiempo real

Resultado esperado:
Un agente funcional capaz de:

Escuchar al usuario
Responder con voz en tiempo real
Mantener una conversación básica