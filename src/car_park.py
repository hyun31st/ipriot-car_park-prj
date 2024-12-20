from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json


class CarPark:
    '''
    The CarPark class manages incoming and outgoing cars using Sensor classes
    It also shows messages to users through the Display class.
    The class uses a configuration file to store details like the location, capacity,
    and log file settings.
    '''
    def __init__(self, location="Unknown",
                 capacity=0,
                 plates=None,
                 sensors=None,
                 displays=None,
                 log_file=Path("log.txt"),
                 config_file=Path("config.json")):

        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        self.write_config()
        self.celsius_temperature = 27

    @property
    def available_bays(self):
        # The available bays will be calculated by subtracting the current number of cars from the total capacity.
        # If the number of cars exceeds the capacity, the following code will show 0 instead of negative number
        return self.capacity - len(self.plates) if len(self.plates) < self.capacity else 0

    @property
    def fahrenheit_temperature(self):
        return (self.celsius_temperature * 9 / 5) + 32

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def unregister(self, display):
        try:
            self.displays.remove(display)
        except ValueError:
            pass

    def update_displays(self):
        data = {"available_bays": self.available_bays,
                "temperature": f"{self.celsius_temperature} degrees Celsius, {self.fahrenheit_temperature:.0f} degrees Fahrenheit"}
        for display in self.displays:
            # display.update(data)
            print(f"updating display {display.id}")
            display.update(data)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate}\t{action}\tat {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    def write_config(self):
        with open(self.config_file, "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)
