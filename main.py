from fastapi import FastAPI
from src.api.routes import pedido_routes
from src.infrastructure.database.database import engine, Base
from src.infrastructure.database import models 

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Raízes do Nordeste - API",
    description="Sistema de gestão multicanal com integração de pagamento Mock e Banco de Dados.",
    version="1.0.0"
)

app.include_router(pedido_routes.router, prefix="/pedidos")

@app.get("/", tags=["Home"])
def home():
    return {"mensagem": "API Raízes do Nordeste ativa, operante e com Banco de Dados conectado!"}