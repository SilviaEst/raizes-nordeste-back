from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infrastructure.database.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String)
    perfil = Column(String) # ADMIN, CLIENTE, etc.
    consentimento_lgpd = Column(Boolean, default=False)

class PedidoModel(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    unidade_id = Column(Integer)
    canal_pedido = Column(String) # RF04
    status = Column(String)
    valor_total = Column(Float)
    data_criacao = Column(DateTime, default=datetime.now)