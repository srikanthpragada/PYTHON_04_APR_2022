# Display no. of days in the given month and year

month = int(input("Enter month :"))
if month == 2:
    year = int(input("Enter year :"))
    if year % 4 == 0:
        nodays = 29
    else:
        nodays = 28
elif month in [4, 6, 9, 11]:
    nodays = 30
else:
    nodays = 31

print("No. of days = ", nodays)
