students = []

while True:
    st = input("Enter marks [end to stop] :")
    if st == "end":
        break
    marks = st.split(":")
    valid_marks = list(filter(str.isdigit, marks))
    total = sum(map(int, valid_marks))
    avg = total / len(valid_marks)
    students.append((total, avg))

for total, avg in students:
    print(f"{total:4} {avg:5.2f}")
