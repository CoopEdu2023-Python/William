class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __str__(self):
        return self.name


stu1 = Student(114514, '小明', 10)
stu2 = Student(114514, '小红', 9)
print(stu1)
print(stu2)
