def average_length(*names):
    total = 0
    for n in names:
        total += len(str(n))

    return total / len(names)


print(average_length("Java" "Python", "C", "C++"))
print(average_length("JavaScript", "Visual Basic"))
print(average_length(10, 20, 500, 6000))
