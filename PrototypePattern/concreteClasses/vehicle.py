import copy
from interface.prototype import Prototype


class Vehicle(Prototype):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def clone(self):
        # Deep copy to avoid shared references
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.color} {self.brand} {self.model}"