import asyncio
import ollama

async def generate_response(text_queue: asyncio.Queue,
                            response_queue: asyncio.Queue):

    loop = asyncio.get_event_loop()

    while True:
        text = await text_queue.get()

        if text.lower() == "salir":
            print("[👋 Cerrando agente...]")
            break

        if not text.strip(): 
            continue

        print("[🧠 Pensando...]")

        def ask_llm():
            response = ollama.chat(
                model='llama3',
                messages=[
                    {
                        'role': 'system',
                        'content': 'Eres un asistente de voz conversacional. Responde de forma breve, natural y amigable. Evita respuestas demasiado largas.'
                    },
                    {
                        'role': 'user',
                        'content': text
                    }
                ]
            )

            return response['message']['content']

        response_text = await loop.run_in_executor(None, ask_llm)

        print(f"[🤖 Respuesta]: {response_text}")

        await response_queue.put(response_text)