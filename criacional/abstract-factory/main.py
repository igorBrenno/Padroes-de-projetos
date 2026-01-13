from abc import ABC, abstractmethod

# Interface da fábrica abstrata
class Botao(ABC):
    @abstractmethod
    def renderizar(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def marcar(self):
        pass

# Produtos concretos para Windows
class WindowsBotao(Botao):
    def renderizar(self):
        return "Renderizando botão no estilo Windows."
    
class WindowsCheckbox(Checkbox):
    def marcar(self):
        return "Marcando checkbox no estilo Windows."


# Produtos concretos para MacOS
class botaoMacOS(Botao):
    def renderizar(self):
        return "Renderizando botão no estilo MacOS."

class MacOSCheckbox(Checkbox):
    def marcar(self):
        return "Marcando checkbox no estilo MacOS."
    
# Interface da fábrica abstrata
class GUIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_checkbox(self) -> Checkbox:
        pass

# Fábricas concretas
class WindowsFactory(GUIFactory):
    def criar_botao(self) -> Botao:
        return WindowsBotao()

    def criar_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def criar_botao(self) -> Botao:
        return botaoMacOS()

    def criar_checkbox(self) -> Checkbox:
        return MacOSCheckbox()
    

def client_code(factory: GUIFactory):
    botao = factory.criar_botao()
    checkbox = factory.criar_checkbox()

    print(botao.renderizar())
    print(checkbox.marcar())

if __name__ == "__main__":
    print("Client: Testando cliente com a fábrica Windows:")
    client_code(WindowsFactory())

    print("\nClient: Testando cliente com a fábrica MacOS:")
    client_code(MacOSFactory())