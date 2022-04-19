def get_number(s):
    if s.isdigit():
        return int(s)
    else:
        return 0


s = "87,66,67,98,,54"

marks = s.split(",")
print(marks)

valid_marks = filter(str.isdigit, marks)
print(sum(map(int, valid_marks)))

print(sum(map(get_number, marks)))
