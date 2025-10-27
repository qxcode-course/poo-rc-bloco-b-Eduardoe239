class Person:
    def __init__(self, n: str, m: int):
        self.__name = n
        self.__money = m

    def getName(self):
        return self.__name
    def getMoney(self):
        return self.__money
    
    def adMoney(self, v: int):
        self.__money -= v
        return f"{self.__name}:{self.__money}"

class Mtuber:
    def __init__(self):
        self.__cost = 0
        self.__driver: Person | None = None
        self.__passenger: Person | None = None

    def __str__(self):
        driver = str(self.__driver) if self.__driver else "None"