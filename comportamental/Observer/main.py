from abc import ABC, abstractmethod

# Interface do Observador (Subscriber)
class Observer(ABC):
    @abstractmethod
    def update(self, mensagem: str):
        pass

# Assunto / Sujeito (Publisher)
class CanalNoticias:
    def __init__(self):
        self._inscritos = []

    def inscrever(self, observador: Observer):
        self._inscritos.append(observador)

    def desinscrever(self, observador: Observer):
        self._inscritos.remove(observador)

    def notificar(self, noticia: str):
        for inscrito in self._inscritos:
            inscrito.update(noticia)

    def nova_manchete(self, texto: str):
        print(f"Canal: Nova notícia postada: {texto}")
        self.notificar(texto)

# Observadores Concretos
class AplicativoMobile(Observer):
    def update(self, mensagem: str):
        print(f"Notificação no Celular: {mensagem}")

class EmailNewsletter(Observer):
    def update(self, mensagem: str):
        print(f"E-mail enviado com a notícia: {mensagem}")

# Código do Cliente
canal_tech = CanalNoticias()

app = AplicativoMobile()
email = EmailNewsletter()

canal_tech.inscrever(app)
canal_tech.inscrever(email)

canal_tech.nova_manchete("Lançamento do novo chip quântico!")

print("\n--- Removendo inscrição de e-mail ---")
canal_tech.desinscrever(email)

canal_tech.nova_manchete("IA supera humanos em testes de lógica.")