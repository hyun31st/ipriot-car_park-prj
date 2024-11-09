print("Executing Sensor Class from sensor.py")

class Sensor:
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"from __str__ method: id = {self.id}, is_active = {self.is_active}, car_park = {self.car_park}"

class EntrySensor(Sensor):
    ...

class ExitSensor(Sensor):
    ...

if __name__ == "__main__":
    sensor = Sensor(id=1, is_active=True, car_park=True)
    print(sensor)