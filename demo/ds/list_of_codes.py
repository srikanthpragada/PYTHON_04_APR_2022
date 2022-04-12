s = "Python"

codes = []
for c in s:
    codes.append(ord(c))

print(codes)

# List comprehension
codes = [ord(c) for c in s if c.islower()]
print(codes)
