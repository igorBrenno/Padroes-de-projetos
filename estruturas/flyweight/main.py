class TipoArvore:
    def __init__(self, nome, cor, textura):
        self.nome = nome
        self.cor = cor
        self.textura = textura

    def desenhar(self, x, y):
        print(f"Desenhando árvore '{self.nome}' ({self.cor}) em [{x}, {y}]")

# Flyweight Factory: Gerencia e garante o reuso dos objetos
class FabricaDeArvores:
    _tipos_arvore = {}

    @classmethod
    def obter_tipo_arvore(cls, nome, cor, textura):
        chave = (nome, cor, textura)
        if chave not in cls._tipos_arvore:
            print(f"--- Criando novo objeto compartilhado: {nome} ---")
            cls._tipos_arvore[chave] = TipoArvore(nome, cor, textura)
        return cls._tipos_arvore[chave]

class Arvore:
    def __init__(self, x, y, tipo: TipoArvore):
        self.x = x
        self.y = y
        self.tipo = tipo

    def desenhar(self):
        self.tipo.desenhar(self.x, self.y)

# Cliente
class Floresta:
    def __init__(self):
        self.arvores = []

    def plantar_arvore(self, x, y, nome, cor, textura):
        # A fábrica garante que não criaremos objetos repetidos para o "TipoArvore"
        tipo = FabricaDeArvores.obter_tipo_arvore(nome, cor, textura)
        arvore = Arvore(x, y, tipo)
        self.arvores.append(arvore)

    def exibir(self):
        for arvore in self.arvores:
            arvore.desenhar()

# Execução
minha_floresta = Floresta()
minha_floresta.plantar_arvore(10, 20, "Carvalho", "Verde", "Rugosa")
minha_floresta.plantar_arvore(15, 25, "Carvalho", "Verde", "Rugosa")
minha_floresta.plantar_arvore(50, 80, "Pinheiro", "Verde Escuro", "Lisa")

print(f"\nTotal de árvores na lista: {len(minha_floresta.arvores)}")
minha_floresta.exibir()