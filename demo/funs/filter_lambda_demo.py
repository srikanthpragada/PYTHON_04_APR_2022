nums = [-10, 30, -50, 33, 88]

for n in filter(lambda v: v > 0, nums):
    print(n)

for n in filter(lambda v: v % 5 == 0, nums):
    print(n)