st = "how did you do yesterday and how are you doing today"

for c in sorted(set(st)):
    print(c, st.count(c))