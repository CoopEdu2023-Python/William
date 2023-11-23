class Vehicle:
    def __init__(self):
        self.brand = None
        self.color = None

    def show_info(self):
        print(self.color, self.brand)


class Car(Vehicle):
    pass
