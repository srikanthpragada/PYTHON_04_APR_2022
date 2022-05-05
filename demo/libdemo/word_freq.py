import re

f = open("old_man.txt", "rt")
contents = f.read()
f.close()

words = re.findall(r'\w+', contents)
print(words)

for word in sorted(set(words)):
    print(f"{word:15}  - {words.count(word)}")
