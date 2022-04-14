
names = ['java', 'python', 'c#', 'sql', 'javascript']
chars = set()   # Empty set

for n in names:
    chars |= set(n)

print(chars)





