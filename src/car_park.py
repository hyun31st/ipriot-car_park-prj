from sensor import Sensor
from display import Display

print("Executing CarPark Class from car_park.py")

class CarPark:
    def __init__(self, location = "Unknown",
                 capacity = "Unknown",
                 plates = None,
                 sensors = None,
                 displays = None):

        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}

    @property
    def available_bays(self):
        ## The available bays will be calculated by subtracting the current number of cars from the total capacity.
        ## If the number of cars exceeds the capacity, the following code will show 0 instead of negative number
        return self.capacity - len(self.plates) if len(self.plates) < self.capacity else 0



if __name__ == "__main__":
    car_park = CarPark("123 Example Street", 2)
    car_park.add_car(('1E222333'))
    car_park.add_car('1E322333')
    car_park.add_car('1E322553')
    print(car_park)
    print("available bays: ",car_park.available_bays)
    display = Display(2, CarPark.available_bays, "Welcome!!", True)
    display.update({"available_bays": CarPark.available_bays, "temperature": 25})
    
