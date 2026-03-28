from fastapi import APIRouter
from models.message import Message
from services.response_handler import gerar_resposta_completa

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
def chat(msg: Message):
    resposta = gerar_resposta_completa(msg.text)

    return {
        "user_id": msg.user_id,
        "pergunta": msg.text,
        "resposta": resposta
    }