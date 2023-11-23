class Vehicle:
    def __init__(self):
        self.brand = 1
        self.color = 2

    def show_info(self):
        print(self.color, self.brand)


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.seat = 3

    def show_info(self):
        print(self.color, self.brand, self.seat)


Car().show_info()