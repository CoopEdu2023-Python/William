class Student:
    def __init__(self, sid, name, grade):
        self.sid = sid
        self.name = name
        self.grade = grade

    def __len__(self):
        return len(self.name)


stu1 = Student(114514, '小明', 10)
print(len(stu1))
