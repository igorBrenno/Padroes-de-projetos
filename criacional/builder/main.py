from abc import ABC, abstractmethod

class Computador:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.armazenamento = None

    def __str__(self):
        return f"PC [CPU: {self.cpu}, GPU: {self.gpu}, RAM: {self.ram}, Disco: {self.armazenamento}]"

# interface do Builder

class ComputadorBuilder(ABC):
    @abstractmethod
    def add_cpu(self): pass

    @abstractmethod
    def add_gpu(self): pass

    @abstractmethod
    def add_ram(self): pass

    @abstractmethod
    def add_armazenamento(self): pass

    @abstractmethod
    def get_computador(self) -> Computador: pass

# builder concreto
class PCGamerBuilder(ComputadorBuilder):
    def __init__(self):
        self.computador = Computador()

    def add_cpu(self):
        self.computador.cpu = "Intel Core i9"
    
    def add_gpu(self):
        self.computador.gpu = "NVIDIA RTX 4090"

    def add_ram(self):
        self.computador.ram = "32GB DDR5"

    def add_armazenamento(self):
        self.computador.armazenamento = "2TB NVMe SSD"

    def get_computador(self) -> Computador:
        return self.computador

# diretor
# O Diretor define a ordem dos passos de construção
class Diretor:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> ComputadorBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ComputadorBuilder):
        self._builder = builder

    def construir_pc_completo(self):
        self.builder.add_cpu()
        self.builder.add_ram()
        self.builder.add_gpu()
        self.builder.add_armazenamento()

# cliente
if __name__ == "__main__":
    diretor = Diretor()
    builder_gamer = PCGamerBuilder()
    
    diretor.builder = builder_gamer
    diretor.construir_pc_completo()
    
    meu_pc = builder_gamer.get_computador()
    print(meu_pc)