import random
import uuid

class PagamentoMock:
    """
    Simulador de Gateway de Pagamento Externo para a Raízes do Nordeste.
    """
    
    @staticmethod
    def processar_pagamento(pedido_id: int, valor: float):  # Simula uma pequena demora de rede
       
        sucesso = random.random() < 0.8   # Simulação de lógica: 80% de chance de aprovação
        
        if sucesso:
            return {
                "status": "APROVADO",
                "transacao_id": str(uuid.uuid4()), # Gera um ID único aleatório
                "mensagem": "Pagamento processado com sucesso pelo Gateway Externo."
            }
        else:
            return {
                "status": "REJEITADO",
                "transacao_id": None,
                "mensagem": "Saldo insuficiente ou falha na comunicação com a operadora."
            }