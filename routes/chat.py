from fastapi import APIRouter, status
from schemas.message import Message
from services.response_handler import gerar_resposta_completa

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/", status_code=status.HTTP_200_OK)
def enviar_mensagem(msg: Message) -> dict:
    
    resposta = gerar_resposta_completa(msg.text)

    return {
        "user_id": msg.user_id,
        "pergunta": msg.text,
        "resposta": resposta
    }