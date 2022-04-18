def add(n1, n2):
    return n1 + n2


print(id(add), type(add))
add2 = add


def add(n1, n2, n3):
    return n1 + n2 + n3


print(id(add))

print(add2(10, 20))
print(add(10, 20, 50))
