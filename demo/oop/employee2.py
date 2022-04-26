class Employee:
    grades = {'A': 30, 'B': 25, 'C': 40}

    # Constructor
    def __init__(self, name, grade, salary=0):
        # Object attributes
        self.name = name
        self.grade = grade
        self.salary = salary

    # Methods
    def getNetSalary(self):
        hraper = Employee.grades[self.grade]
        return self.salary + self.salary * hraper / 100

    def setGrade(self, grade):
        self.grade = grade

    def setSalary(self, salary):
        self.salary = salary

    def __str__(self):
        return f"{self.name:20} {self.grade} {self.salary}"


e1 = Employee("Anders", "C", 50000)  # create an object/instance
print(e1)
print(e1.getNetSalary())
