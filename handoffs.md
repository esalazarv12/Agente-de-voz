Sprint Actual.

Se implementó un agente conversacional de voz en tiempo real utilizando Python puro y programación asíncrona con asyncio.

Componentes construidos
Captura de audio desde micrófono
Transcripción local con Whisper
Integración de LLM local mediante Ollama + llama3
Conversión de texto a voz con pyttsx3
Pipeline concurrente usando asyncio.Queue
Decisiones arquitectónicas consolidadas
Arquitectura modular desacoplada
Comunicación mediante colas async
Procesamiento local offline
Uso de asyncio.gather() para concurrencia
Problemas detectados
El sistema puede capturar el audio del propio TTS
No existe Voice Activity Detection
No hay control de estado del pipeline
Próximos pasos
Implementar VAD
Mejorar sincronización de audio
Agregar memoria conversacional
Optimizar latencia del loop
