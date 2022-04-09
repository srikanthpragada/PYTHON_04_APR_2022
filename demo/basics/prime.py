# print factors for the given number
num = 195
for i in range(2, num//2 + 1):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")


