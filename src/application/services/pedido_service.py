from src.domain.entities.pedido import Pedido
from src.infrastructure.external_services.pagamento_mock import PagamentoMock

class PedidoService:
    """
    Orquestrador de pedidos da Raízes do Nordeste.
    Coordena o fluxo entre a API, o Domínio e a Infraestrutura.
    """

    def criar_e_processar_pedido(self, pedido_data: Pedido):
        print(f"--- Iniciando processamento do pedido via {pedido_data.canal_pedido} ---")
        
        # 1. Simulação de Validação de Estoque (Regra de Domínio)
        print(f"Validando estoque para a unidade {pedido_data.unidade_id}...")
        
        # 2. Chamada ao Gateway de Pagamento (Infraestrutura)
        print("Solicitando processamento financeiro ao Mock...")
        resultado_pagamento = PagamentoMock.processar_pagamento(
            pedido_id=1, # Simulado
            valor=pedido_data.valor_total
        )
        
        # 3. Atualização de Status baseada no resultado
        if resultado_pagamento["status"] == "APROVADO":
            pedido_data.status = "PAGO / AGUARDANDO PREPARO"
            print(f"Sucesso: {resultado_pagamento['mensagem']}")
        else:
            pedido_data.status = "CANCELADO / PAGAMENTO REJEITADO"
            print(f"Falha: {resultado_pagamento['mensagem']}")
            
        return {
            "pedido": pedido_data,
            "pagamento_info": resultado_pagamento
        }