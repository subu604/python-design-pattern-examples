from StrategyPattern.interface.DriveStrategy import DriveStrategy

class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print("Driving with normal strategy: Smooth and efficient ride.")