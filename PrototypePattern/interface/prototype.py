from abc import ABC, abstractmethod

# Step 1: Strategy Interface
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass