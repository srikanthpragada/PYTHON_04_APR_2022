# Compare two files and display result

with open("f1.txt", "rt") as f1, open("f2.txt", "rt") as f2:
    found = False
    row = 1
    col = 1
    while True:
        ch1 = f1.read(1)  # read one char
        ch2 = f2.read(1)
        if ch1 == '' and ch2 == '':
            break

        if ch1 != ch2:
            print(f'Differs at row {row} and col {col}')
            found = True
            break

        if ch1 == '\n':
            row += 1
            col = 1
        else:
            col += 1

if not found:
    print("Same Contents")
