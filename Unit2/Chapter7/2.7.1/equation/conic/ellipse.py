from math import pi


class Circle:
    def __init__(self):
        self.radius = float()

    def parameter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * (self.radius**2)


class Ellipse:
    def __init__(self):
        self.major_axis = float()
        self.minor_axis = float()

    def perimeter(self):
        pass

    def area(self):
        return self.minor_axis * self.major_axis * pi

