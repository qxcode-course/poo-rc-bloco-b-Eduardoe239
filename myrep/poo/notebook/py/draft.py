class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

def getCarga(self) -> int:
    return self.__carga

def getCapacidade(self) -> int:
    return self.__capacidade

def descarregar(self, tempo: int) -> int:
    if self.__carga == 0:
        return 0
    usado = min(self.__carga, tempo)
    self.__carga -= usado
    return usado

def carregar(self, tempo: int):
    self.__carga = min(self.__capacidade, self.__carga + tempo)

def mostrar(self):
    print(f"({self.__carga}/{self.__capacidade})")


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def getPotencia(self):
        print(f"(Potencia {self.__potencia})")

class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None