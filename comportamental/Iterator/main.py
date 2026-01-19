from collections.abc import Iterable, Iterator

# Iterador Concreto
# Define a lógica de como percorrer a coleção
class OrdemReversaIterator(Iterator):
    def __init__(self, colecao):
        self._colecao = colecao
        # Começa pelo último índice
        self._posicao = len(colecao) - 1

    def __next__(self):
        if self._posicao >= 0:
            valor = self._colecao[self._posicao]
            self._posicao -= 1
            return valor
        raise StopIteration()

# A Coleção Concreta
class ListaNomes(Iterable):
    def __init__(self):
        self._itens = []

    def adicionar_item(self, item):
        self._itens.append(item)

    def __iter__(self):
        # Retornamos nosso iterador personalizado
        return OrdemReversaIterator(self._itens)

# Código do Cliente
nomes = ListaNomes()
nomes.adicionar_item("Alice")
nomes.adicionar_item("Bruno")
nomes.adicionar_item("Caio")

print("Percorrendo a lista em ordem reversa:")
for nome in nomes:
    print(f"-> {nome}")