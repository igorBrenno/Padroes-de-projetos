from abc import ABC, abstractmethod

# Interface do Visitor
class Visitor(ABC):
    @abstractmethod
    def visitar_desenvolvedor(self, desenvolvedor):
        pass

    @abstractmethod
    def visitar_gerente(self, gerente):
        pass

# Interface do Elemento (Aceita o visitante)
class Funcionario(ABC):
    @abstractmethod
    def aceitar(self, visitor: Visitor):
        pass

# Elementos Concretos
class Desenvolvedor(Funcionario):
    def __init__(self, nome, total_linhas_codigo):
        self.nome = nome
        self.total_linhas_codigo = total_linhas_codigo

    def aceitar(self, visitor: Visitor):
        visitor.visitar_desenvolvedor(self)

class Gerente(Funcionario):
    def __init__(self, nome, total_projetos):
        self.nome = nome
        self.total_projetos = total_projetos

    def aceitar(self, visitor: Visitor):
        visitor.visitar_gerente(self)

# Visitantes Concretos (Novas operações)
class RelatorioPerformance(Visitor):
    def visitar_desenvolvedor(self, dev):
        print(f"Relatório Dev {dev.nome}: Escreveu {dev.total_linhas_codigo} linhas.")

    def visitar_gerente(self, ger):
        print(f"Relatório Gerente {ger.nome}: Gerencia {ger.total_projetos} projetos.")

class AjusteSalarial(Visitor):
    def visitar_desenvolvedor(self, dev):
        print(f"Calculando bônus para {dev.nome} baseado em código.")

    def visitar_gerente(self, ger):
        print(f"Calculando bônus para {ger.nome} baseado em metas de projeto.")

# Código do Cliente
equipe = [
    Desenvolvedor("Alice", 5000),
    Gerente("Bob", 3),
    Desenvolvedor("Carlos", 1200)
]

print("--- Gerando Relatórios ---")
relatorio = RelatorioPerformance()
for f in equipe:
    f.aceitar(relatorio)

print("\n--- Calculando Ajustes ---")
ajuste = AjusteSalarial()
for f in equipe:
    f.aceitar(ajuste)