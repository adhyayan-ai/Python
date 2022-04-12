class Vehicle:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def go(self, time, distance):
        print(f"Your {self.model} traveled {distance} miles in {time} minutes")


    def stop(self):
        print(f"Your {self.model} stopped.")


car = Vehicle("Honda", "Blue")
car.go(30, 30)