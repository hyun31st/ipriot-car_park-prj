print("Executing Display Class from display.py")

class Display:
    def __init__(self, id, car_park, message = "", is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.id}: Welcome to the car park."

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    display = Display(1, 'North Metro Park')
    print(display)
    display.update({"message": "Goodbye"})


