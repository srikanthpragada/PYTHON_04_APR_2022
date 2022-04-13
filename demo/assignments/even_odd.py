# Accept 10 numbers and display all even numbers first and then odd numbers

evens = []
odds = []

for i in range(1, 6):
    n = int(input("Enter number :"))
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

for n in evens + odds:
    print(n)
