from abc import ABC, abstractmethod

# Interface do Mediador
class TorreDeControle(ABC):
    @abstractmethod
    def enviar_mensagem(self, mensagem, aeronave):
        pass

# Classe Base para os Componentes
class Aeronave(ABC):
    def __init__(self, torre: TorreDeControle, identificador: str):
        self.torre = torre
        self.identificador = identificador

    @abstractmethod
    def receber(self, mensagem):
        pass

# Componentes Concretos
class Aviao(Aeronave):
    def enviar(self, mensagem):
        print(f"✈️ {self.identificador} enviando: {mensagem}")
        self.torre.enviar_mensagem(mensagem, self)

    def receber(self, mensagem):
        print(f"📩 {self.identificador} recebeu da torre: {mensagem}")

# Mediador Concreto
class TorreConcreta(TorreDeControle):
    def __init__(self):
        self._aeronaves = []

    def registrar_aeronave(self, aeronave: Aeronave):
        self._aeronaves.append(aeronave)

    def enviar_mensagem(self, mensagem, remetente):
        for aeronave in self._aeronaves:
            # O mediador garante que o remetente não receba sua própria mensagem
            if aeronave != remetente:
                aeronave.receber(mensagem)

# Código do Cliente
torre = TorreConcreta()

aviao1 = Aviao(torre, "Voo 101")
aviao2 = Aviao(torre, "Voo 202")
aviao3 = Aviao(torre, "Voo 303")

torre.registrar_aeronave(aviao1)
torre.registrar_aeronave(aviao2)
torre.registrar_aeronave(aviao3)

# Os aviões não se conhecem, eles apenas interagem com a torre
aviao1.enviar("Solicitando autorização para pouso.")