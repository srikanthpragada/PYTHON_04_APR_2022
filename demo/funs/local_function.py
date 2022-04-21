g = 100  # Global variable


# Enclosing function
def f1():
    a = 1  # Enclosing variable
    print("f1()")

    # Local function
    def f2():
        b = 2  # Local variable
        nonlocal a
        a = 10
        print("f2()", a, b, g)

    f2()
    print(a)


f1()
