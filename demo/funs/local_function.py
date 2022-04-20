g = 100  # Global variable


# Enclosing function
def f1():
    a = 1  # Enclosing variable
    print("f1()")

    # Local function
    def f2():
        b = 2  # Local variable
        print("f2()", a, b, g)

    f2()


f1()
