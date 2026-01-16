from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool: pass
    
    @abstractmethod
    def enable(self): pass
    
    @abstractmethod
    def disable(self): pass

class TV(Device):
    def __init__(self): self._on = False
    def is_enabled(self): return self._on
    def enable(self): self._on = True; print("TV: Ligada")
    def disable(self): self._on = False; print("TV: Desligada")

class Radio(Device):
    def __init__(self): self._on = False
    def is_enabled(self): return self._on
    def enable(self): self._on = True; print("Rádio: Ligado")
    def disable(self): self._on = False; print("Rádio: Desligado")


# A interface que o usuário usa
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

# Abstração Refinada
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Dispositivo: Modo Mudo Ativado")


if __name__ == "__main__":
    tv = TV()
    controle_simples = RemoteControl(tv)
    print("Testando TV com controle simples:")
    controle_simples.toggle_power()

    print("\n" + "-"*30 + "\n")

    radio = Radio()
    controle_avancado = AdvancedRemoteControl(radio)
    print("Testando Rádio com controle avançado:")
    controle_avancado.toggle_power()
    controle_avancado.mute()