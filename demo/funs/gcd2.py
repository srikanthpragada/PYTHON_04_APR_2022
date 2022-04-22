# Take two numbers on command line and display GCD of 2 numbers

import sys
import math

if len(sys.argv) < 3:
    print("Usage : python gcd.py number1 number2")
    exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(math.gcd(num1, num2))
