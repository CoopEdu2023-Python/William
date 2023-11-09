class Student:
    name = None

    def drop(self):
        pass


stu1 = Student()
stu1.name = '小明'
stu2 = Student()
stu2.name = '小红'
print(type(stu1), type(stu2), type(stu1.name), type(stu2.name), type(stu2.drop()))