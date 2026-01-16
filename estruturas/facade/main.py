# Subsistemas Complexos
class Projetor:
    def ligar(self): print("Projetor: Ligado")
    def modo_cinema(self): print("Projetor: Ajustado para 4K HDR")

class Som:
    def ligar(self): print("Som: Ligado")
    def definir_volume(self, nivel): print(f"Som: Volume em {nivel}")

class Streaming:
    def conectar(self): print("Streaming: Conectado ao servidor")
    def reproduzir(self, filme): print(f"Streaming: Iniciando '{filme}'")

# Facade (A Fachada)
class HomeTheaterFacade:
    def __init__(self, projetor, som, streaming):
        self.projetor = projetor
        self.som = som
        self.streaming = streaming

    def assistir_filme(self, filme):
        print("\n--- Preparando Cinema em Casa ---")
        self.projetor.ligar()
        self.projetor.modo_cinema()
        self.som.ligar()
        self.som.definir_volume(10)
        self.streaming.conectar()
        self.streaming.reproduzir(filme)
        print("--- Bom Filme! ---\n")

# Sem o Facade, o cliente teria que instanciar e configurar 3 classes e 6 métodos manualmente.
meu_projetor = Projetor()
meu_som = Som()
meu_player = Streaming()

# Usando a Fachada
cinema_casa = HomeTheaterFacade(meu_projetor, meu_som, meu_player)
cinema_casa.assistir_filme("Interestelar")