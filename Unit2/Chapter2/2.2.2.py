class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __del__(self):
        print(f'student: {self.name}')


stu1 = Student(114514, '小明', 10)
stu2 = Student(114514, '小红', 9)
del stu1
del stu2
