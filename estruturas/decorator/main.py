from abc import ABC, abstractmethod

# Interface do componente
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem: str):
        pass

# Componente concreto
class NotificadorEmail(Notificador):
    def __init__(self, email: str):
        self.email = email

    def enviar(self, mensagem: str):
        print(f"Enviando e-mail para {self.email}: {mensagem}")

# Decorador base
class NotificadorDecorator(Notificador):
    def __init__(self, notificador: Notificador):
        self._notificador = notificador

    def enviar(self, mensagem: str):
        self._notificador.enviar(mensagem)

# Decoradores concretos
class SMSDecorator(NotificadorDecorator):
    def __init__(self, notificador: Notificador, telefone: str):
        super().__init__(notificador)
        self.telefone = telefone

    def enviar(self, mensagem: str):
        super().enviar(mensagem)
        print(f"Enviando SMS para {self.telefone}: {mensagem}")


class FacebookDecorator(NotificadorDecorator):
    def __init__(self, notificador: Notificador, usuario_fb: str):
        super().__init__(notificador)
        self.usuario_fb = usuario_fb

    def enviar(self, mensagem: str):
        super().enviar(mensagem)
        print(f"Enviando mensagem no Facebook para {self.usuario_fb}: {mensagem}")


if __name__ == "__main__":
    notificador = NotificadorEmail("to@hupefni.np")

    notificador = SMSDecorator(notificador, "83 586636665")
    notificador = FacebookDecorator(notificador, "DuaneOmelhor")

    notificador.enviar("Alerta: Sistema fora do ar!")
