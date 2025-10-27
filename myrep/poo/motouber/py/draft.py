class Person:
    def __init__(self, name: str, money: int):
        self.__name = name
        self.__money = money

    def getName(self):
        return self.__name

    def getMoney(self):
        return self.__money

    def addMoney(self, value: int):
        self.__money += value

    def pay(self, value: int):
        self.__money -= value

    def __str__(self):
        return f"{self.__name}:{self.__money}"


class MtUber:
    def __init__(self):
        self.__cost = 0
        self.__driver: Person | None = None
        self.__passenger: Person | None = None

    def __str__(self):
        driver = str(self.__driver) if self.__driver else "None"
        passenger = str(self.__passenger) if self.__passenger else "None"
        return f"Cost: {self.__cost}, Driver: {driver}, Passenger: {passenger}"

    def setDriver(self, driver: Person):
        self.__driver = driver

    def setPassenger(self, passenger: Person):
        self.__passenger = passenger

    def drive(self, cost: int):
        if self.__driver is None or self.__passenger is None:
            return
        self.__cost += cost

    def leavePassenger(self):
        if self.__passenger is None:
            return
        passenger_money = self.__passenger.getMoney()
        if passenger_money >= self.__cost:
            self.__passenger.pay(self.__cost)
            self.__driver.addMoney(self.__cost)
            print(f"{self.__passenger.getName()}:{self.__passenger.getMoney()} left")
        else:
            print("fail: Passenger does not have enough money")
            self.__passenger.pay(passenger_money)
            print(f"{self.__passenger.getName()}:0 left")
            self.__driver.addMoney(self.__cost)
        self.__cost = 0
        self.__passenger = None


def main():
    moto = MtUber()
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(moto)
        elif args[0] == "setDriver":
            name = args[1]
            money = int(args[2])
            driver = Person(name, money)
            moto.setDriver(driver)
        elif args[0] == "setPass":
            name = args[1]
            money = int(args[2])
            passenger = Person(name, money)
            moto.setPassenger(passenger)
        elif args[0] == "drive":
            value = int(args[1])
            moto.drive(value)
        elif args[0] == "leavePass":
            moto.leavePassenger()


main()
