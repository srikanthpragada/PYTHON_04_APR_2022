def ispositive(n):
    return n > 0


nums = [-10, 30, -50, 33, 88]

for n in filter(ispositive, nums):
    print(n)

for c in filter(str.isupper, "SomeUpperCase"):
    print(c)