from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


def main():
    moondalup_car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")
    moondalup_entry_sensor = EntrySensor(1, True, moondalup_car_park)
    moondalup_exit_sensor = ExitSensor(2, True, moondalup_car_park)
    moondalup_display = Display(1, moondalup_car_park, "Welcome to Moondalup", True)

    print(moondalup_car_park)
    print(moondalup_display)

    for i in range(0, 3):
        moondalup_car_park.register(moondalup_display)
        moondalup_entry_sensor.detect_vehicle()

    for i in range(0, 2):
        moondalup_exit_sensor.detect_vehicle()


if __name__ == "__main__":
    main()
