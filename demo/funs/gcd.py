# Take two numbers on command line and display GCD of 2 numbers

import sys

if len(sys.argv) < 3:
    print("Usage : python gcd.py number1 number2")
    exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

smallest = min(num1, num2)
if num1 % smallest == 0 and num2 % smallest == 0:
    print(smallest)
    exit()

for i in range(smallest//2, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        exit()




