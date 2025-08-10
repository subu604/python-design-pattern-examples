from StrategyPattern.main.vehicle import Vehicle
from StrategyPattern.concreteClasses.sportsStrategy import SportsDriveStrategy
from StrategyPattern.concreteClasses.normalStrategy import NormalDriveStrategy

if __name__ == "__main__":
    # Sports car with sports driving strategy
    sports_car = Vehicle(SportsDriveStrategy())
    sports_car.drive()

    # Sedan with normal driving strategy
    sedan = Vehicle(NormalDriveStrategy())
    sedan.drive()

    # Switching strategies dynamically
    print("\nSwitching Sedan to sports mode...")
    sedan = Vehicle(SportsDriveStrategy())
    sedan.drive()
