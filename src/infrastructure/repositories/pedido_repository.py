from sqlalchemy.orm import Session
from datetime import datetime
from src.infrastructure.database.models.models import PedidoModel 

def salvar_pedido_no_banco(db: Session, dados_do_pedido: dict):
   
    novo_pedido = PedidoModel(
        usuario_id=dados_do_pedido.get("usuario_id"),
        unidade_id=dados_do_pedido.get("unidade_id"),
        canal_pedido=dados_do_pedido.get("canal_pedido"),
        valor_total=dados_do_pedido.get("valor_total"),
        status="PAGO", 
        data_criacao=datetime.now()
    )
    
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    
    return novo_pedido