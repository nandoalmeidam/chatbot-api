from fastapi import FastAPI
from routes.chat import router as chat_router

app = FastAPI(
    title="Chatbot API com IA",
    description="API de atendimento automatizado com integração de IA",
    version="1.0.0"
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {"status": "Chatbot rodando"}