# Print smallest of 3 numbers

a, b, c = 10, 2, 1
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
elif b < c:
    print(b)
else:
    print(c)
