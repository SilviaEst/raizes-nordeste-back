from pydantic import BaseModel
from typing import Optional

class Estoque(BaseModel):
    id: Optional[int] = None      # O ID pode ser nulo se o banco ainda não o gerou
    unidade_id: int               # Referência à loja (FK)
    produto_id: int               # Referência ao cuscuz/tapioca (FK)
    quantidade: int               # Quantidade física disponível

    class Config:
        from_attributes = True    # Permite que o Pydantic leia dados do banco (ORM)