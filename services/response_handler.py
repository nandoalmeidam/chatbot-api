from services.ia_service import gerar_resposta_ia

def gerar_resposta_completa(texto: str) -> str:
    resposta = gerar_resposta_ia(texto)

    if not resposta:
        return "Não consegui responder no momento."

    return resposta