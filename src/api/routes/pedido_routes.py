from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List 
from src.domain.entities.pedido import Pedido, RespostaPedidoCriado
from src.application.services.pedido_service import PedidoService
from src.infrastructure.database.database import get_db 

router = APIRouter()
service = PedidoService()

@router.post("/", response_model=RespostaPedidoCriado, tags=["Pedidos"], status_code=status.HTTP_201_CREATED)
def criar_novo_pedido(pedido: Pedido, db: Session = Depends(get_db)): 
    resultado = service.criar_e_processar_pedido(pedido, db) 
    return resultado

@router.get("/", response_model=List[Pedido], tags=["Pedidos"])
def listar_todos_os_pedidos(db: Session = Depends(get_db)):
    
    return service.listar_pedidos(db)


@router.patch("/{pedido_id}/status", tags=["Pedidos"])
def atualizar_status_do_pedido(pedido_id: int, novo_status: str, db: Session = Depends(get_db)):

    return service.atualizar_status(pedido_id, novo_status, db)