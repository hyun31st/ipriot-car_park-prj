from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


def main():
    '''
    main function of the CarPark project.

    This CarPark system is using Object-Oriented Programming (OOP) concepts in Python.
    The system is consist of a car park, sensors, and displays to track the cars entering and
    exiting and the availability of parking bays.
    '''
    moondalup_car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")
    moondalup_entry_sensor = EntrySensor(1, True, moondalup_car_park)
    moondalup_exit_sensor = ExitSensor(2, True, moondalup_car_park)
    moondalup_display = Display(1, moondalup_car_park, "Welcome to Moondalup", True)

    print(moondalup_car_park)
    print(moondalup_display)

    moondalup_car_park.register(moondalup_entry_sensor)
    moondalup_car_park.register(moondalup_exit_sensor)
    moondalup_car_park.register(moondalup_display)

    for i in range(0, 10):
        moondalup_entry_sensor.detect_vehicle()

    for i in range(0, 2):
        moondalup_exit_sensor.detect_vehicle()


if __name__ == "__main__":
    main()
