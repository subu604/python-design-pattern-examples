from abc import ABC, abstractmethod

# Step 1: Strategy Interface
class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass