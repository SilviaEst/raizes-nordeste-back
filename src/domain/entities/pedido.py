from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from enum import Enum

class CanalPedido(str, Enum):
    APP = "APP"
    TOTEM = "TOTEM"
    BALCAO = "BALCAO"
    PICKUP = "PICKUP"
    WEB = "WEB"

class ItemPedido(BaseModel):
    produto_id: int
    quantidade: int
    preco_unitario: float

class Pedido(BaseModel):
    id: Optional[int] = None
    usuario_id: int
    unidade_id: int
    canal_pedido: CanalPedido
    status: str = "RECEBIDO"
    valor_total: float
    data_criacao: datetime = datetime.now()
    itens: Optional[List[ItemPedido]] = [] 

    class Config:
        from_attributes = True

class RespostaPedidoCriado(BaseModel):
    pedido: Pedido
    pagamento_info: dict

    class Config:
        from_attributes = True