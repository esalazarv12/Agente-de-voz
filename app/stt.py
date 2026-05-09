import asyncio
import tempfile
import soundfile as sf
import os
import whisper

# cargar modelo una sola vez
print("[🧠 Cargando modelo Whisper...]")
model = whisper.load_model("base")

async def speech_to_text(audio_queue: asyncio.Queue, text_queue: asyncio.Queue):
    loop = asyncio.get_event_loop()

    while True:
        audio = await audio_queue.get()

        print("[📝 Transcribiendo...]")

        # crear archivo temporal
        fd, path = tempfile.mkstemp(suffix=".wav")
        os.close(fd)

        try:
            # guardar audio
            sf.write(path, audio, 16000)

            # whisper es bloqueante → thread separado
            def transcribe():
                result = model.transcribe(path, language="es")
                return result["text"]

            text = await loop.run_in_executor(None, transcribe)

        finally:
            os.remove(path)

        text = text.strip()

        if len(text) < 2:
            continue

        print(f"[📝 Texto]: {text}")

        await text_queue.put(text)