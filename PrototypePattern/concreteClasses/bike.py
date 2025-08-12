import copy
from interface.prototype import Prototype

class Bike(Prototype):
    def __init__(self, brand, cc):
        self.brand = brand
        self.cc = cc

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.cc}cc {self.brand} Bike"