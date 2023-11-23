class A:
    def __init__(self):
        self.X = 1
        self.Y = 2
        self.Z = 3

    def get_x(self):
        print(self.X)


class B(A):
    def get_y(self):
        print(self.Y)


class C(B):
    def get_z(self):
        print(self.Z)


a = A()
b = B()
c = C()
a.get_x()
b.get_x()
b.get_y()
c.get_x()
c.get_y()
c.get_z()