class Person:
    def __init__(self, name):

        if len(name) < 10:
            self.__name = name
        else:
            self.name = name
