# print factors for the given number on command-line

import sys

if len(sys.argv) < 2:
    # print("Usage : python factors.py  number")
    # exit()
    num = int(input("Enter number :"))
else:
    num = int(sys.argv[1])

for i in range(2, num // 2 + 1):
    if num % i == 0:
        print(i)
