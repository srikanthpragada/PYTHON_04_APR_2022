class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # private attribute

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __int__(self):
        return self.age


p1 = Person("Larry", 30)
p2 = Person("Bill", 45)
p3 = Person("Steve", 25)
print(p1)  # str(p1) ->  p1.__str__()
print(p1 == p2)  # p1.__eq__(p2)
# print(p1 > p3)  # p1.__gt__(p3)

for p in sorted((p1, p2, p3)):
    print(p)
