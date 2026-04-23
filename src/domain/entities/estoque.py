from pydantic import BaseModel
from typing import Optional

class Estoque(BaseModel):
    id: Optional[int] = None      
    unidade_id: int               
    produto_id: int               
    quantidade: int              

    class Config:
        from_attributes = True    