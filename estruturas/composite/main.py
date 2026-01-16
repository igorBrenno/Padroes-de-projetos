from abc import ABC, abstractmethod

# Componente Base
class SistemaArquivo(ABC):
    @abstractmethod
    def exibir(self, indentacao=0):
        pass

# Folha - Objeto individual
class Arquivo(SistemaArquivo):
    def __init__(self, nome):
        self.nome = nome

    def exibir(self, indentacao=0):
        print("  " * indentacao + f" Arquivo: {self.nome}")

# Composto (Composite) - Objeto que contém outros componentes
class Pasta(SistemaArquivo):
    def __init__(self, nome):
        self.nome = nome
        self.filhos = []

    def adicionar(self, componente: SistemaArquivo):
        self.filhos.append(componente)

    def remover(self, componente: SistemaArquivo):
        self.filhos.remove(componente)

    def exibir(self, indentacao=0):
        print("  " * indentacao + f" Pasta: {self.nome}")
        for filho in self.filhos:
            filho.exibir(indentacao + 1)

# Criando arquivos individuais
doc1 = Arquivo("curriculo.pdf")
doc2 = Arquivo("foto_ferias.jpg")
doc3 = Arquivo("notas.txt")

# Criando pastas e montando a árvore
pasta_documentos = Pasta("Meus Documentos")
pasta_fotos = Pasta("Fotos")

pasta_fotos.adicionar(doc2)
pasta_documentos.adicionar(doc1)
pasta_documentos.adicionar(pasta_fotos) # Pasta dentro de pasta
pasta_documentos.adicionar(doc3)

# O cliente trata tudo como ComponenteSistemaArquivos
pasta_documentos.exibir()