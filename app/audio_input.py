import sounddevice as sd
import numpy as np
import asyncio

SAMPLE_RATE = 16000
DURATION = 4

DEVICE_ID = 1

async def capture_audio(audio_queue: asyncio.Queue):
    loop = asyncio.get_event_loop()

    while True:
        print("[🎤 Escuchando...]")

        audio = await loop.run_in_executor(
            None,
            lambda: sd.rec(
                int(DURATION * SAMPLE_RATE),
                samplerate=SAMPLE_RATE,
                channels=1,
                dtype='float32',
                device=DEVICE_ID
            )
        )

        await loop.run_in_executor(None, sd.wait)

        print("[✅ Audio capturado]")

        audio = np.squeeze(audio)

        await audio_queue.put(audio)