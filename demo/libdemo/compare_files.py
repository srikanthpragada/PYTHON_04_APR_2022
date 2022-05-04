f1 = open("f1.txt", "rt")
f2 = open("f2.txt", "rt")

found = False
row = 1
for firstline in f1.readlines():
    secondline = f2.readline()
    # Exit if second file is shorter than first
    if len(secondline) == 0:  # EOF on second file
        print(f'Differ in row {row}, col 1')
        found = True
        break

    col = 0
    for fch in firstline:
        if col < len(secondline):
            sch = secondline[col]
            if sch != fch:
                print(f'Differ in row {row}, col {col + 1}')
                found = True
                break
        else:
            print(f'Differ in row {row}, col {col + 1}')
            found = True
            break

        col += 1

    # Come out of outer loop if chars diff
    if found:
        break
    elif len(secondline) > col:
        print(f'Differ in row {row}, col {col + 1}')
        found = True
        break

    row += 1

if not found:
    # Do we have lines in second file
    secondline = f2.readline()
    if len(secondline) != 0:
        print(f'Differ in row {row}, col 1')
    else:
        print("Same Contents")

f1.close()
f2.close()
