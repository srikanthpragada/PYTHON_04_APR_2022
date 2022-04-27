class Doctor:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def __str__(self):
        return f"{self.name},{self.dept}"


class ResidentDoctor (Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()},{self.salary}"

    def get_salary(self):
        return self.salary


r = ResidentDoctor("Dr. Jane", "Ped", 400000)
print(r)
