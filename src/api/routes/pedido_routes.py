from fastapi import APIRouter
from src.domain.entities.pedido import Pedido
from src.application.services.pedido_service import PedidoService

router = APIRouter()
service = PedidoService()

@router.post("/", response_model=dict, tags=["Pedidos"])
def criar_novo_pedido(pedido: Pedido):
    """
    Endpoint para criação de pedidos multicanal.
    Recebe os dados, valida o canal e processa o pagamento via Mock.
    """
    resultado = service.criar_e_processar_pedido(pedido)
    return resultado