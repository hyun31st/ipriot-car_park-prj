from abc import ABC, abstractmethod
from datetime import datetime
import random


class Sensor(ABC):
    '''
    The Sensor class is used to detect incoming and outgoing cars from the car park.
    It also generates a fake number plate for demonstration purposes.
    This is an abstract class and should not be instantiated.
    '''
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"from __str__ method: id = {self.id}, is_active = {self.is_active}, car_park = {self.car_park}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    # Create fake car number plates
    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    '''
    The EntrySensor class is inherited from Sensor class.
    This class detects incoming cars and updates the car park system
    with the number plate.
    '''
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected at {datetime.now():%Y-%m-%d %H:%M:%S}. Plate: {plate}\n")


class ExitSensor(Sensor):
    '''
    The ExitSensor class is inherited from Sensor class.
    This class detects outgoing cars from the car park and updates the car park system
    with the number plate.
    '''
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected at {datetime.now():%Y-%m-%d %H:%M:%S}. Plate: {plate}\n")


    def _scan_plate(self):

        return random.choice(self.car_park.plates)


if __name__ == "__main__":
    sensor = EntrySensor(id=1, is_active=True, car_park=True)
    print(sensor)
