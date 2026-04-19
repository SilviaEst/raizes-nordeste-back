from fastapi import APIRouter, status
from src.domain.entities.pedido import Pedido
from src.application.services.pedido_service import PedidoService

router = APIRouter()
service = PedidoService()

@router.post("/", response_model=dict, tags=["Pedidos"], status_code=status.HTTP_201_CREATED)
def criar_novo_pedido(pedido: Pedido):
    resultado = service.criar_e_processar_pedido(pedido)
    return resultado

@router.get("/", response_model=list, tags=["Pedidos"])
def listar_todos_os_pedidos():
    return service.listar_pedidos()