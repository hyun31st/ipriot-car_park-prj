from abc import ABC, abstractmethod
from datetime import datetime
import random


class Sensor(ABC):
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
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected at {datetime.now():%Y-%m-%d %H:%M:%S}. Plate: {plate}")


class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected at {datetime.now():%Y-%m-%d %H:%M:%S}. Plate: {plate}")


    def _scan_plate(self):

        return random.choice(self.car_park.plates)


if __name__ == "__main__":
    sensor = EntrySensor(id=1, is_active=True, car_park=True)
    print(sensor)
