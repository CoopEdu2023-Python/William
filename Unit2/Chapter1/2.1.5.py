class Pow:
    x = None
    n = None

    def p(self):
        return self.x ** self.n


calculate = Pow()
calculate.n = 7
calculate.x = 7
print(calculate.p())
