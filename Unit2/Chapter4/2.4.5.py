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

    def get