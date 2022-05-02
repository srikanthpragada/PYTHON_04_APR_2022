# Read names from names.txt

with open("names.txt", "rt") as f:
    for line in f.readlines():
        # print(line, end = '')
        print(line.strip())
