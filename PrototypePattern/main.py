from concreteClasses.bike import Bike
from concreteClasses.vehicle import Vehicle

if __name__ == "__main__":
    # Create original objects
    car1 = Vehicle("Tesla", "Model S", "Red")
    bike1 = Bike("Yamaha", 150)

    print("Original Car:", car1)
    print("Original Bike:", bike1)

    # Clone them
    car2 = car1.clone()
    car2.color = "Blue"

    bike2 = bike1.clone()
    bike2.cc = 200

    print("\nCloned Car:", car2)
    print("Cloned Bike:", bike2)

    print("\nOriginal Car (unchanged):", car1)
    print("Original Bike (unchanged):", bike1)