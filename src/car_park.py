print("Executing CarPark Class from car_park.py")

class CarPark:
    def __init__(self, location = "Unknown",
                 capacity = "Unknown",
                 plates = None,
                 sensors = None,
                 displays = None):

        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.sensors = sensors or []
        self.displays = displays
    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays"

if __name__ == "__main__":
    car_park = CarPark("123 Example Street", 100)
    print(car_park)