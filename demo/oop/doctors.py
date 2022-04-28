from abc import ABC, abstractmethod


class Doctor(ABC):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def __str__(self):
        return f"{self.name},{self.dept}"

    @abstractmethod
    def get_salary(self):
        pass


class ResidentDoctor(Doctor):
    def __init__(self, name, dept, salary):
        super().__init__(name, dept)
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()},{self.salary}"

    def get_salary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, dept, visits, charge):
        super().__init__(name, dept)
        self.visits = visits
        self.charge = charge

    def __str__(self):
        return f"{super().__str__()},{self.visits},{self.charge}"

    def get_salary(self):
        return self.visits * self.charge


r = ResidentDoctor("Dr. Jane", "Ped", 400000)
print(r)

c = Consultant("Dr. Dean", "GYN", 10, 1500)
print(c)
print(c.get_salary())
