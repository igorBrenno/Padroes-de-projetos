# Memento (O snapshot do estado)
class Memento:
    def __init__(self, estado: str):
        self._estado = estado

    def get_estado(self):
        return self._estado

# Originator (O objeto cujo estado queremos salvar)
class EditorTexto:
    def __init__(self):
        self._conteudo = ""

    def escrever(self, texto):
        self._conteudo += texto

    def exibir(self):
        print(f"Conteúdo atual: '{self._conteudo}'")

    def salvar(self) -> Memento:
        print("--- Salvando estado... ---")
        return Memento(self._conteudo)

    def restaurar(self, memento: Memento):
        self._conteudo = memento.get_estado()
        print("--- Estado restaurado! ---")

# Caretaker (Responsável por guardar os Mementos)
class Historico:
    def __init__(self, editor: EditorTexto):
        self._mementos = []
        self._editor = editor

    def fazer_backup(self):
        self._mementos.append(self._editor.salvar())

    def desfazer(self):
        if not self._mementos:
            print("Nada para desfazer.")
            return
        
        memento = self._mementos.pop()
        self._editor.restaurar(memento)

# Código do Cliente
editor = EditorTexto()
historico = Historico(editor)

editor.escrever("Olá, ")
historico.fazer_backup()

editor.escrever("este é o padrão Memento.")
editor.exibir()

historico.desfazer()
editor.exibir()