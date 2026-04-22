from sqlalchemy.orm import Session
from src.domain.entities.pedido import Pedido
from src.infrastructure.external_services.pagamento_mock import PagamentoMock
from src.infrastructure.repositories.pedido_repository import salvar_pedido_no_banco
from src.infrastructure.database.models.models import PedidoModel

class PedidoService:

    def criar_e_processar_pedido(self, pedido_data: Pedido, db: Session):
        print(f"--- Iniciando processamento do pedido via {pedido_data.canal_pedido} ---")
        
        dados_para_banco = {
            "usuario_id": pedido_data.usuario_id,
            "unidade_id": pedido_data.unidade_id,
            "canal_pedido": pedido_data.canal_pedido,
            "valor_total": pedido_data.valor_total
        }

        pedido_db = salvar_pedido_no_banco(db, dados_para_banco)
        
        print(f"Solicitando processamento financeiro para o pedido ID: {pedido_db.id}...")
        resultado_pagamento = PagamentoMock.processar_pagamento(
            pedido_id=pedido_db.id, 
            valor=pedido_db.valor_total
        )
        
        if resultado_pagamento["status"] == "APROVADO":
            pedido_db.status = "PAGO / AGUARDANDO PREPARO"
        else:
            pedido_db.status = "CANCELADO / PAGAMENTO REJEITADO"
            
        db.commit()
        db.refresh(pedido_db)
            
        return {
            "pedido": pedido_db,
            "pagamento_info": resultado_pagamento
        }
    
    def listar_pedidos(self, db: Session):
        return db.query(PedidoModel).all()