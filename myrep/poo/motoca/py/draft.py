class Pessoa:
    def __init__(self, nome: str, age: int):
        self.__name = nome
        self.__age = age
    
    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name
    def __str__(self):
        return f"{self.__name}:{self.__age}"
    
class Motoca:
    def __init__(self, potencia: int = 1):
        self.__potencia = potencia
        self.__time : int = 0
        self.__pessoa = None

    def __str__(self):
        if self.__pessoa is not None:
            return f"power:{self.__potencia}, time:{self.__time}, person:({self.__pessoa})"
        else:
            return f"power:{self.__potencia}, time:{self.__time}, person:(empty)"
    
    def inserir(self, pessoa:Pessoa) -> bool:
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = pessoa
        return True

    def remover(self):
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return None
        pessoa_rem = self.__pessoa
        self.__pessoa = None
        return pessoa_rem
    
    def buyTime(self, time: int):
        self.__time += time

    def drive(self, timer: int):
        if self.__time == 0:
            print("fail: buy time first")
            return
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return
        if self.__pessoa.getAge() > 10:
            print("fail: too old to drive")
            return
        if timer > self.__time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
        else:
            self.__time -= timer

    def honk(self):
        return "P" + ("e" * self.__potencia) + "m"
        
def main():
    moto = Motoca()
    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "init":
            potencia = int(args[1])
            moto = Motoca(potencia)
        elif args[0] == "enter":
            name = args[1]
            idade = int(args[2])
            pessoa = Pessoa(name, idade)
            moto.inserir(pessoa)
        elif args[0] == "leave":
            pessoa = moto.remover()
            if pessoa is not None:
                print(pessoa)
        elif args[0] == "buy":
            moto.buyTime(int(args[1]))
        elif args[0] == "drive":
            time = int(args[1])
            moto.drive(time)
        elif args[0] == "honk":
            print(moto.honk())

main()