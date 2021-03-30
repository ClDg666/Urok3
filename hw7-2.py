
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod         # задаём шаблон для наследников название метода расчета количества ткани
    def calculate(self):
        pass


class Coat(Clothes):

    @property              #
    def calculate(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.param) + 0.3)


coat = Coat(45)
suit = Suit(170)
print(coat.calculate)
print(suit.calculate)