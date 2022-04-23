class Employee:
    # Constructor
    def __init__(self, name, grade, salary=0):
        # Object attributes
        self.name = name
        self.grade = grade
        self.salary = salary

    # Methods
    def getNetSalary(self):
        if self.grade == 'A':
            return self.salary + self.salary * 30 / 100
        else:
            return self.salary + self.salary * 25 / 100

    def setGrade(self, grade):
        self.grade = grade

    def setSalary(self, salary):
        self.salary = salary


e1 = Employee("Anders", "A", 50000)  # create an object/instance
print(e1.__dict__)
print(e1.getNetSalary())  # calling method
e1.setGrade('B')
print(e1.getNetSalary())

e2 = Employee("Rossum", "B")
e2.salary = 55000
print(e2.__dict__)
