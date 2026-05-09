import asyncio

from app.audio_input import capture_audio
from app.stt import speech_to_text
from app.llm import generate_response
from app.tts import text_to_speech

async def main():
    audio_queue = asyncio.Queue()
    text_queue = asyncio.Queue()
    response_queue = asyncio.Queue()

    await asyncio.gather(
        capture_audio(audio_queue),
        speech_to_text(audio_queue, text_queue),
        generate_response(text_queue, response_queue),
        text_to_speech(response_queue),
    )

if __name__ == "__main__":
    asyncio.run(main())