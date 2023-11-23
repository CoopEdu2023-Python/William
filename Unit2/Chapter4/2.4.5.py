class Shape:
    def __init__(self):
        self.color = 'red'

    def get_color(self):
        print(self.color)

    def set_color(self, c):
        self.color = c


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.length = 4
        self.width = 5

    def get_perimeter(self):
        print(2*(self.length+self.width))

    def get_area(self):
        print(self.length * self.width)


r = Rectangle()
r.get_area()
r.get_perimeter()