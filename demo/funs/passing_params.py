# immutable object
def zero(n):
    print("Id of n = ", id(n))
    n = 0
    print("Id of n = ", id(n))


# Mutable object
def prepend(lst, value):
    lst.insert(0, value)


a = 100
print("Id of a = ", id(a))
zero(a)
print(a)  # 100 or 0??

l = [10, 20]
prepend(l, 5)
print(l)
