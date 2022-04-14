# display all common char among all strings
names = ['typescript', 'javascript', 'c#', 'c++', 'c']
chars = set(names[0])

for n in names[1:]:
    chars &= set(n)

print(chars)
