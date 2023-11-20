class Student:
    def __init__(self, sid, name, grade, n):
        self.sid = sid
        self.name = name
        self.grade = grade
        self.n = n

    def __eq__(self, other):
        return self.n == other.n


stu1 = Student(114514, '小明', 10, 95)
stu2 = Student(114514, '小红', 9, 90)
print(stu1 == stu2)
