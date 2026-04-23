from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    preco_unitario: float
    categoria: str # Tapioca, Cuscuz, Bebida, etc.

    class Config:
        from_attributes = True