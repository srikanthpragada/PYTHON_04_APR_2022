def math_op(n1, n2, op):
    return op(n1, n2)


def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


print(math_op(10, 20, mul))
print(math_op(10, 20, add))
print(math_op(10, 20, print))
# print(math_op(10, 20, len))