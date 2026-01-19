from abc import ABC, abstractmethod

# Interface de Estado
class EstadoPedido(ABC):
    @abstractmethod
    def avancar(self, pedido):
        pass

    @abstractmethod
    def cancelar(self, pedido):
        pass

# Estados Concretos
class EstadoPendente(EstadoPedido):
    def avancar(self, pedido):
        print("Pagamento confirmado. Mudando para estado: PAGO.")
        pedido.set_estado(EstadoPago())

    def cancelar(self, pedido):
        print("Pedido pendente cancelado com sucesso.")

class EstadoPago(EstadoPedido):
    def avancar(self, pedido):
        print("Pedido enviado para a transportadora. Mudando para estado: ENVIADO.")
        pedido.set_estado(EstadoEnviado())

    def cancelar(self, pedido):
        print("Estornando pagamento... Pedido cancelado.")

class EstadoEnviado(EstadoPedido):
    def avancar(self, pedido):
        print("O pedido já foi enviado e não pode mais avançar de status aqui.")

    def cancelar(self, pedido):
        print("Erro: Não é possível cancelar um pedido que já foi enviado.")

# Contexto (O Pedido)
class Pedido:
    def __init__(self):
        # Estado inicial
        self._estado = EstadoPendente()

    def set_estado(self, estado: EstadoPedido):
        self._estado = estado

    def avancar(self):
        self._estado.avancar(self)

    def cancelar(self):
        self._estado.cancelar(self)

# Código do Cliente
meu_pedido = Pedido()

meu_pedido.avancar()
meu_pedido.avancar() 
meu_pedido.cancelar() 