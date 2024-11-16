class Display:
    def __init__(self, id, car_park, message = "", is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.id}: Welcome to the car park.\n"

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
            print(f"{key}: {value}")
            #self.message = value


if __name__ == "__main__":
    display = Display(1,"Welcome to the car park",True)
    print(display)
    display.update({"message": "Goodbye"})


