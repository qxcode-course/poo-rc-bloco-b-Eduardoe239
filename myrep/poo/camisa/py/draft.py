class Camisa:
    def __init__(self):
        self.__Tamanho: str = ""

    def getTamanho(self):
        return self.__Tamanho
    
    def setTamanho(self, V: str):
        if V in["PP", "P", "M", "G", "GG", "GX"]:
            self.__Tamanho = V
        else:
            print("Fail: valor roupa nao encontrado")
def main():
    camisa = Camisa()

    while camisa.getTamanho() == "":
        tamanho = input(": ")
        camisa.setTamanho(tamanho)
    print("Parabens, voce comprou uma camisa tamanho", camisa.getTamanho())
main()
        