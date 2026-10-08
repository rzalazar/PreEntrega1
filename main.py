import asyncio
from dotenv import load_dotenv

from schemas import ChatMessage, ModelConfig
from clients import AsyncLLMManager

load_dotenv()

async def main():
    prompt = [ChatMessage(role="user", content="¿Qué es la entropía? Responde en 2 oraciones.")]
    
    # --- PRUEBA OPENAI ---
    print("========================================")
    print("PROBANDO OPENAI")
    print("========================================")
    try:
        openai_config = ModelConfig(model_name="gpt-4o-mini", temperature=0.5, max_tokens=150)
        openai_manager = AsyncLLMManager(provider="openai")

        print("\n--- Modo Normal ---")
        response_openai = await openai_manager.generate(prompt, openai_config)
        print(f"Respuesta ({response_openai.provider} - {response_openai.model}):")
        print(response_openai.content)

        print("\n--- Modo Streaming ---")
        print("Respuesta: ", end="", flush=True)
        async for chunk in openai_manager.generate_stream(prompt, openai_config):
            print(chunk, end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"Error en OpenAI: {e}\n")

    # --- PRUEBA ANTHROPIC ---
    print("========================================")
    print("PROBANDO ANTHROPIC")
    print("========================================")
    try:
        anthropic_config = ModelConfig(model_name="claude-3-5-haiku-20241022", temperature=0.5, max_tokens=150)
        anthropic_manager = AsyncLLMManager(provider="anthropic")

        print("\n--- Modo Normal ---")
        response_anthropic = await anthropic_manager.generate(prompt, anthropic_config)
        print(f"Respuesta ({response_anthropic.provider} - {response_anthropic.model}):")
        print(response_anthropic.content)

        print("\n--- Modo Streaming ---")
        print("Respuesta: ", end="", flush=True)
        async for chunk in anthropic_manager.generate_stream(prompt, anthropic_config):
            print(chunk, end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"Error en Anthropic: {e}\n")

if __name__ == "__main__":
    asyncio.run(main())