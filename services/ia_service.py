import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY não encontrada no .env")

client = Groq(api_key=api_key)

def gerar_resposta_ia(texto: str) -> str:
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um atendente da empresa TechStore.\n"
                        "Responda de forma objetiva, profissional e com no máximo 2 frases.\n\n"

                        "Informações da empresa:\n"
                        "- Funcionamento: segunda a sexta, das 9h às 18h\n"
                        "- Sábado: das 9h às 13h\n"
                        "- Produto principal: softwares e soluções digitais\n"
                        "- Preços: variam conforme o serviço, sempre peça mais detalhes\n\n"

                        "Sempre conduza a conversa para entender a necessidade do cliente e avançar no atendimento."
                        
                        "Se o cliente perguntar preço, peça mais informações antes de responder."
)
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