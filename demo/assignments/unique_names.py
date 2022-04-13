
names = []

while True:
    name = input("Enter name [end to stop] : ")
    if name.lower() == 'end':
        break

    # check whether name is already present
    if not name in names:
        names.append(name)


for name in names:
    print(name)