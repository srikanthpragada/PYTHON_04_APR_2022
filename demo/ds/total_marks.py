marks = "90,87,66,56,a,49,87"

total = 0
for n in marks.split(","):
    if n.isdigit():
       total += int(n)

print(total)