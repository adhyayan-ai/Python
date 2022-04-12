class Vehicle:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __repr__(self):
        return f"A {self.color} {self.model}"

    def go(self, time, distance):
        print(f"Your {self.model} traveled {distance} miles in {time} minutes")


    def stop(self):
        print(f"Your {self.model} stopped.")

    def vehicleModel(self):
        return f"Your vehicle is a {self.model}"

car = Vehicle("Toyota", "Black")
print(car)
print(car.vehicleModel())