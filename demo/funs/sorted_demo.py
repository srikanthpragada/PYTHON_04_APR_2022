nums = [-10, 30, -50, 33, 88]

print(sorted(nums))
print(sorted(nums, key=abs))

names = ["Scott", "Mark", "Li", "Jason", "Anders"]

print(sorted(names))
print(sorted(names, key=len))
print(sorted(map(len, names)))
