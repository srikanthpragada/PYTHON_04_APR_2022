num = int(input("Enter a number:"))
count = 0
for i in range(2, num // 2 + 1):
    if num % i == 0:
        count += 1

if count > 0:
    print(f"Number of factors for {num} is {count}")
else:
    print("Entered number is a prime number")
