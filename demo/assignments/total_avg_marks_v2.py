
data = ("56:87:99", "87:abc:98", "87:99", "87:55;55:66")

for st in data:
    marks = st.split(":")
    valid_marks = list(filter(str.isdigit, marks))
    total = sum(map(int, valid_marks))
    avg = total / len(valid_marks)
    print(f"{total:4} {avg:5.2f}")
