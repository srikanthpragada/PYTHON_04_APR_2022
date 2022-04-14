l1 = [98, 33, 44, 54]
l2 = [88, 3, 44, 55, 66]

if len(l1) > len(l2):
    big = l1
    small = l2
else:
    big = l2
    small = l1

for idx, value in enumerate(big):
    if idx < len(small):
        print(value, small[idx])
    else:
        print(value, 0)
