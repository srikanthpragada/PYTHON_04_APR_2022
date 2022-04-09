# print factors for the given number

num = 252
found = False
for i in range(2, num//2 + 1):
    if num % i == 0:
        print(i)
        found = True
        break

if not found:
    print(num)

