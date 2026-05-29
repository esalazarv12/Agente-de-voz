# 🎯 La Bala Trazadora (Tracer Bullet) y el Enrutamiento de Skills

# 📌 Exploración Inicial del Problema

Antes de desarrollar el sistema, se identificó que el principal desafío técnico no era construir módulos aislados, sino lograr que todos los componentes del pipeline conversacional funcionaran de manera coordinada en tiempo real.

Inicialmente se asumía que integrar Speech-to-Text, LLM y Text-to-Speech sería relativamente directo. Sin embargo, durante el análisis temprano del problema se detectaron múltiples riesgos:

* Bloqueo del loop principal
* Latencia excesiva entre módulos
* Captura accidental del audio del propio agente
* Dependencias entre componentes async
* Problemas de concurrencia

El análisis previo permitió redefinir la arquitectura hacia un modelo completamente desacoplado basado en `asyncio.Queue`.

---

# 🧠 Refinamiento del Árbol de Diseño

Durante la fase de exploración se reorganizó el sistema en módulos independientes:

* Captura de audio
* Speech-to-Text
* Generación de respuestas
* Text-to-Speech

Cada componente quedó conectado mediante colas asíncronas, evitando dependencias directas entre módulos.

Esta decisión redujo significativamente el acoplamiento y permitió evolucionar cada componente de forma aislada.

---

# 🎯 Aplicación de la Estrategia “Tracer Bullet”

Siguiendo la analogía de la Bala Trazadora descrita en ingeniería de software, se decidió atacar primero el punto de integración más incierto y riesgoso del sistema:

```text id="b3"
La ejecución concurrente del pipeline completo:
Micrófono → Whisper → Ollama → TTS
```

En lugar de optimizar componentes individuales desde el inicio, se priorizó validar rápidamente si toda la arquitectura podía funcionar extremo a extremo.

Esta decisión permitió detectar tempranamente:

* Problemas de compatibilidad con dispositivos de audio
* Dependencias externas faltantes (FFmpeg)
* Bloqueos del loop async
* Problemas de sincronización entre módulos

---

# 🚀 Feedback Temprano de Arquitectura

La validación temprana del pipeline completo proporcionó retroalimentación inmediata sobre la viabilidad del diseño.

Gracias a esto se tomaron decisiones importantes:

* Uso obligatorio de programación asíncrona
* Separación estricta por responsabilidades
* Eliminación de llamadas bloqueantes
* Uso de procesamiento local offline

Esto evitó construir una arquitectura incorrecta antes de escalar el sistema.

---

# ✅ Resultado

La estrategia de Bala Trazadora permitió validar rápidamente el núcleo crítico del proyecto y reducir el riesgo arquitectónico desde las primeras etapas del desarrollo.

El sistema evolucionó sobre una base funcional real en lugar de depender de diseño teórico no validado.
