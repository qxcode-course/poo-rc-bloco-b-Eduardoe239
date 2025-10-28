class Carregador:
    def __init__(self, potencia: int):
        self.potencia = potencia

    def __str__(self):
        return f"Carregador {self.potencia}W"


class Bateria:
    def __init__(self, carga_max: int):
        self.carga_max = carga_max
        self.carga = carga_max

    def usar(self, minutos: int):
        if self.carga == 0:
            return False
        self.carga -= minutos
        if self.carga < 0:
            self.carga = 0
        return True

    def carregar(self, minutos: int, potencia: int):
        self.carga += minutos * potencia
        if self.carga > self.carga_max:
            self.carga = self.carga_max

    def __str__(self):
        return f"Bateria {self.carga}/{self.carga_max}"
class Notebook:
    def __init__(self):
        self.ligado = False
        self.tempo = 0
        self.carregador = None
        self.bateria = None

    def ligar(self):
        if self.ligado:
            return
        if self.carregador is not None or (self.bateria is not None and self.bateria.carga > 0):
            self.ligado = True
        else:
            print("fail: não foi possível ligar")

    def desligar(self):
        self.ligado = False

    def usar(self, minutos: int):
        if not self.ligado:
            print("fail: desligado")
            return
        self.tempo += minutos
        if self.bateria is not None and self.carregador is None:
            if not self.bateria.usar(minutos):
                print("fail: descarregou")
                self.ligado = False
                return
            if self.bateria.carga == 0:
                print("fail: descarregou")
                self.ligado = False
        elif self.bateria is not None and self.carregador is not None:
            self.bateria.carregar(minutos, self.carregador.potencia)

    def mostrar(self):
        estado = "ligado" if self.ligado else "desligado"
        msg = f"Notebook: {estado}"
        if self.ligado:
            msg += f" por {self.tempo} min"
        if self.carregador is not None:
            msg += f", {self.carregador}"
        if self.bateria is not None:
            msg += f", {self.bateria}"
        print(msg)

    def conectar_carregador(self, potencia: int):
        if self.carregador is not None:
            print("fail: carregador já conectado")
        else:
            self.carregador = Carregador(potencia)

    def remover_carregador(self):
        if self.carregador is None:
            print("fail: Sem carregador")
        else:
            print(f"Removido {self.carregador.potencia}W")
            self.carregador = None
            if self.bateria is None:
                self.ligado = False

    def conectar_bateria(self, carga_max: int):
        if self.bateria is not None:
            print("fail: bateria já conectada")
        else:
            self.bateria = Bateria(carga_max)

    def remover_bateria(self):
        if self.bateria is None:
            print("fail: Sem bateria")
        else:
            print(f"Removido {self.bateria.carga}/{self.bateria.carga_max}")
            self.bateria = None
            if self.carregador is None:
                self.ligado = False

def main():
    note = Notebook()
    while True:
        comando = input().strip().split()
        if len(comando) == 0:
            continue
        acao = comando[0]
        print(f"${' '.join(comando)}")
        if acao == "end":
            break
        elif acao == "show":
            note.mostrar()
        elif acao == "turn_on":
            note.ligar()
        elif acao == "turn_off":
            note.desligar()
        elif acao == "use":
            note.usar(int(comando[1]))
        elif acao == "set_charger":
            note.conectar_carregador(int(comando[1]))
        elif acao == "rm_charger":
            note.remover_carregador()
        elif acao == "set_battery":
            note.conectar_bateria(int(comando[1]))
        elif acao == "rm_battery":
            note.remover_bateria()
        else:
            print("fail: comando inválido")

main()

