import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

print("API KEY:", os.getenv("GROQ_API_KEY"))

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def gerar_resposta_ia(texto: str) -> str:
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "Você é um atendente de uma empresa. Responda de forma objetiva, profissional e curta."
                },
                {
                    "role": "user",
                    "content": texto
                }
            ],
            model="llama-3.1-8b-instant"
        )

        return response.choices[0].message.content
    
    except Exception as e:
        return f"Erro detalhado: {str(e)}"