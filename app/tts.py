import asyncio
import pyttsx3

# inicializar motor TTS
engine = pyttsx3.init()

# velocidad de voz
engine.setProperty('rate', 170)

# volumen
engine.setProperty('volume', 1.0)

async def text_to_speech(response_queue: asyncio.Queue):
    loop = asyncio.get_event_loop()

    while True:
        response = await response_queue.get()

        print("[🔊 Hablando...]")

        def speak():
            engine.say(response)
            engine.runAndWait()

        await loop.run_in_executor(None, speak)