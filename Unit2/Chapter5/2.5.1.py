class Duck:
    def quack(self):
        print("这鸭子正在嘎嘎叫")

    def feathers(self):
        print("这鸭子拥有白色和灰色的羽毛")


class Person:
    def quack(self):
        print("这人正在模仿鸭子")

    def feathers(self):
        print("这人在地上拿起1根羽毛然后给其他人看")


def in_the_forest(duck):
    duck.quack()
    duck.feathers()


def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)


game()
'''
Explain the polymorphism in the code below: 这是一个鸭子类型，因为它完成某个行为时，使用不同的对象会得到不同的状态，所以是多态。
Explain what the statement '物件是一个鸭子' means, as described in Wikipedia: 比如一个鸟会游泳长得和鸭子很像，这个物件一个鸭子。
'''