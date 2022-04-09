num = int(input("Enter a number:"))
count = 0
i = 2
while i <= num//2:
    if num % i == 0:
        count += 1

    i += 1

if count > 0:
    print(f"Number of factors for {num} is {count}")
else:
    print("Entered number is a prime number")
