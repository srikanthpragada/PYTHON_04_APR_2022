marks = "90,87,66,56,49,87"

total = 0
for n in marks.split(","):
    total += int(n)

print(total)