from pydantic import BaseModel, EmailStr
from typing import Optional

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    email: EmailStr
    perfil: str # ADMIN, CLIENTE, COZINHA, etc.
    consentimento_lgpd: bool = False

    class Config:
        from_attributes = True