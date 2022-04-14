l1 = [98, 33, 44, 54, 99, 20, 30]
l2 = [88, 3, 44, 55, 66]

for idx, value in enumerate(l1):
    if idx < len(l2):
        print(value, l2[idx])
    else:
        print(value, 0)
