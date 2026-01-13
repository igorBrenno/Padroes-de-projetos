import copy
from abc import ABC, abstractmethod

# interface do protótipo
class Protótipo(ABC):
    @abstractmethod
    def clonar(self):
        pass

# classe concreta que implementa o protótipo
class Documento(Protótipo):
    def __init__(self, titulo: str, conteudo: str):
        self.titulo = titulo
        self.conteudo = conteudo
        self.metadados = {"autor": "Sistema", "versao": "1.0"}

    def clonar(self):
        # Usamos o copy.deepcopy para garantir que listas e dicionários
        # internos também sejam copiados, e não apenas referenciados.
        return copy.deepcopy(self)

    def __str__(self):
        return f"Documento [Título: {self.titulo}, Versão: {self.metadados['versao']}]"

# código cliente
if __name__ == "__main__":
    # 1. Criamos um objeto "caro" ou base
    doc_original = Documento("Relatório Mensal", "Conteúdo muito longo...")
    
    # 2. Em vez de criar um novo do zero, clonamos
    doc_copia = doc_original.clonar()
    doc_copia.titulo = "Relatório Mensal (Cópia)"
    doc_copia.metadados["versao"] = "1.1"

    # Verificação
    print(f"Original: {doc_original}")
    print(f"Cópia:    {doc_copia}")
    
    print(f"\nOs objetos são o mesmo na memória? {doc_original is doc_copia}")