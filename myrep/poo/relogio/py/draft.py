class Watch:
    def __init__(self, hora: int = 0, min: int = 0, seg: int = 0):
        self.__hora = 0
        self.__min = 0
        self.__seg = 0

        self.setHora(hora)
        self.setMin(min)
        self.setSeg(seg)

    def getHora(self):
        return self.__hora
    def getMin(self):
        return self.__min
    def getSeg(self):
        return self.__seg
    
    def setHora(self, H: int):
        if H >= 0 and H <= 23:
            self.__hora = H
        else:
            print("fail: hora invalida")
    def setMin(self, M: int):
        if M >= 0 and M <= 59:
            self.__min = M
        else:
            print("fail: minuto invalido")
    def setSeg(self, S: int):
        if S >= 0 and S <= 59:
            self.__seg = S
        else:
            print("fail: segundo invalido")

    def nextSecond(self):
        self.__seg += 1
        if self.__seg > 59:
            self.__seg = 0
            self.__min += 1
            if self.__min > 59:
                self.__min = 0
                self.__hora += 1
                if self.__hora > 23:
                    self.__hora = 0

    def __str__(self):
        return f"{self.__hora:02d}:{self.__min:02d}:{self.__seg:02d}"
    
def main():
    relog = Watch()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print(relog)
        if args[0] == "init":
            H, M, S = map(int, args[1:])
            relog = Watch(H, M, S)

        if args[0] == "set":
            H, M, S = map(int, args[1:])
            relog.setHora(H)
            relog.setMin(M)
            relog.setSeg(S)
        
        if args[0] == "next":
            relog.nextSecond()

main()