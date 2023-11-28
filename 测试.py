# 多态： 多种状态，即完成某个行为时，使用不同的对象会得到不同的状态。

class Animal:  # 抽象类
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('汪汪汪')


class Cat(Animal):
    def speak(self):
        print('喵喵喵')


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

# 抽象类：含有抽象方法的类称之为抽象类
# 抽象方法：方法体是空实现的（pass）称之为抽象方法