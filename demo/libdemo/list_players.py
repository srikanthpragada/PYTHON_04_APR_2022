from datetime import datetime

with open("players.txt", "rt") as f:
    today = datetime.now()
    players = {}
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue

        name, dobstr = parts
        try:
            dob = datetime.strptime(dobstr, '%Y-%m-%d')
            age = (today - dob).days // 365
            players[name] = age
        except:
            pass

for name, age in sorted(players.items(), key=lambda t: t[1]):
    print(f"{name:30} {age}")
