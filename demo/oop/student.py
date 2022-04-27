class Student:
    courses = {'python': 10000, 'java': 15000, 'sql': 5000}

    @staticmethod
    def getFee(course):
        return Student.courses.get(course, None)

    def __init__(self, name, course):
        self.name = name
        if not course in Student.courses:
            raise ValueError("Invalid course name")

        self.course = course
        self.feepaid = 0

    def payment(self, amount):
        self.feepaid += amount

    def due(self):
        return Student.courses[self.course] - self.feepaid

    def __str__(self):
        return f"{self.name}, {self.course}, {self.feepaid}"


s = Student("Joe", "java")
s.payment(5000)
print(s.due())

print(Student.getFee("java"), Student.getFee("javaee"))
