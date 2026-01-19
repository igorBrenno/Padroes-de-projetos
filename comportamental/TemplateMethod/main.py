from abc import ABC, abstractmethod

# Classe Abstrata com o Template Method
class BebidaQuente(ABC):
    # Template de ações a serem seguidas
    def preparar_receita(self):
        self.ferver_agua()
        self.infusao()
        self.colocar_na_xicara()
        self.adicionar_condimentos()

    # Passos comuns (já implementados)
    def ferver_agua(self):
        print("Fervendo a água...")

    def colocar_na_xicara(self):
        print("Despejando na xícara...")

    # Passos que as subclasses DEVEM implementar
    @abstractmethod
    def infusao(self):
        pass

    @abstractmethod
    def adicionar_condimentos(self):
        pass

# Implementação Concreta: Café
class Cafe(BebidaQuente):
    def infusao(self):
        print("Passando o café pelo filtro...")

    def adicionar_condimentos(self):
        print("Adicionando açúcar e leite.")

# Implementação Concreta: Chá
class Cha(BebidaQuente):
    def infusao(self):
        print("Mergulhando o sachê de chá...")

    def adicionar_condimentos(self):
        print("Adicionando limão.")

# Código do Cliente 
print("--- Preparando Café ---")
cafe = Cafe()
cafe.preparar_receita()

print("\n--- Preparando Chá ---")
cha = Cha()
cha.preparar_receita()