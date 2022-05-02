# Display marks list by taking data from marks.txt

with open("marks.txt", "rt") as f:
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue

        name = parts[0]
        marks = parts[1:]
        valid_marks = list(filter(str.isdigit, marks))
        total = sum(map(int, valid_marks))
        avg = total / len(valid_marks)
        print(f"{name:10} {total:4}  {avg:5.2f}")
