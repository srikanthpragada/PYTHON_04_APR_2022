
a = 100
try:
    b = int(input("Enter number :"))
    c = a // b
    print(c)
except ValueError as ex:
    print("Invalid number! -->", ex)
except ZeroDivisionError:
    print("Number cannot be zero!")
except Exception as ex:
    print("Something went wrong!", ex)

print("The End")
