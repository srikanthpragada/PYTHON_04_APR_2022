class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private attribute

    def getAge(self):
        return self.__age


p = Person("Larry", 30)
print(p.getAge())
print(p.__dict__)
print(p.name, p._Person__age)
