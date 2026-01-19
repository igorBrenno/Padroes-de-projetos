from abc import ABC, abstractmethod

# Interface Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver
class Luz:
    def ligar(self):
        print("Luz: Ligada! 💡")

    def desligar(self):
        print("Luz: Desligada! 🌑")

# Comandos Concretos
class ComandoLigarLuz(Command):
    def __init__(self, luz: Luz):
        self.luz = luz

    def execute(self):
        self.luz.ligar()

    def undo(self):
        self.luz.desligar()

class ComandoDesligarLuz(Command):
    def __init__(self, luz: Luz):
        self.luz = luz

    def execute(self):
        self.luz.desligar()

    def undo(self):
        self.luz.ligar()

# Invoker - O disparador que guarda o comando
class ControleRemoto:
    def __init__(self):
        self._historico = []

    def pressionar_botao(self, comando: Command):
        comando.execute()
        self._historico.append(comando)

    def pressionar_desfazer(self):
        if self._historico:
            comando = self._historico.pop()
            print("Desfazendo última ação...")
            comando.undo()
        else:
            print("Nada para desfazer.")

# Cliente
luz_da_sala = Luz()
controle = ControleRemoto()

ligar = ComandoLigarLuz(luz_da_sala)
desligar = ComandoDesligarLuz(luz_da_sala)

controle.pressionar_botao(ligar)
controle.pressionar_botao(desligar)
controle.pressionar_desfazer()