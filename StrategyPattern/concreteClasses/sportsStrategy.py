from StrategyPattern.interface.DriveStrategy import DriveStrategy

class SportsDriveStrategy(DriveStrategy):
    def drive(self):
        print("Driving with sports strategy: High speed and performance!")