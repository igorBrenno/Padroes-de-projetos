from abc import ABC, abstractmethod

# Interface Comum
class Documento(ABC):
    @abstractmethod
    def exibir(self):
        pass

# Objeto Real - A entidade pesada que queremos controlar o acesso
class DocumentoReal(Documento):
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self._carregar_do_disco()

    def _carregar_do_disco(self):
        print(f"💾 Carregando arquivo pesado: {self.nome_arquivo}...")

    def exibir(self):
        print(f"📄 Conteúdo do documento: {self.nome_arquivo}")

# Proxy (Procurador) - Controla o acesso ao DocumentoReal
class DocumentoProxy(Documento):
    def __init__(self, nome_arquivo, usuario_role):
        self.nome_arquivo = nome_arquivo
        self.usuario_role = usuario_role
        self._documento_real = None

    def exibir(self):
        # Controle de Acesso
        if self.usuario_role != "ADMIN":
            print(f"❌ Acesso Negado: O usuário não tem permissão para ver '{self.nome_arquivo}'.")
            return

        # Inicialização sob demanda (Virtual Proxy)
        if self._documento_real is None:
            self._documento_real = DocumentoReal(self.nome_arquivo)
        
        self._documento_real.exibir()

# Código do Cliente
print("Tentativa com usuário comum")
doc1 = DocumentoProxy("relatorio_financeiro.pdf", "USER")
doc1.exibir()

print("\nTentativa com usuário admin")
doc2 = DocumentoProxy("relatorio_financeiro.pdf", "ADMIN")
# O carregamento só acontece aqui, quando realmente necessário
doc2.exibir()