from abc import ABC, abstractmethod

# Interface Strategy Estratégia Comum
class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self, peso: float) -> float:
        pass

# Estratégias Concretas
class FreteSedex(EstrategiaFrete):
    def calcular(self, peso: float) -> float:
        return peso * 5.0 + 10.0

class FreteLoggi(EstrategiaFrete):
    def calcular(self, peso: float) -> float:
        return peso * 3.5 + 5.0

class FreteRetirada(EstrategiaFrete):
    def calcular(self, peso: float) -> float:
        return 0.0

# Contexto o Carrinho de Compras
class CarrinhoDeCompras:
    def __init__(self, peso_total: float):
        self.peso_total = peso_total
        self._estrategia_frete = None

    def definir_estrategia_frete(self, estrategia: EstrategiaFrete):
        self._estrategia_frete = estrategia

    def calcular_total_frete(self):
        if not self._estrategia_frete:
            print("Por favor, selecione um método de frete.")
            return
        
        valor = self._estrategia_frete.calcular(self.peso_total)
        print(f"O valor do frete para {self.peso_total}kg é: R$ {valor:.2f}")

# Código do Cliente 
carrinho = CarrinhoDeCompras(peso_total=2.5)

# O cliente escolhe a estratégia em tempo de execução
carrinho.definir_estrategia_frete(FreteSedex())
carrinho.calcular_total_frete()

carrinho.definir_estrategia_frete(FreteLoggi())
carrinho.calcular_total_frete()

carrinho.definir_estrategia_frete(FreteRetirada())
carrinho.calcular_total_frete()