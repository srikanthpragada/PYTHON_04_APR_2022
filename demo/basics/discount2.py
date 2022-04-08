# Take price and calculate discount

price = int(input("Enter price :"))
if price > 10000:
    disrate = 0.30
elif price > 5000:
    disrate = 0.20
elif price > 2000:
    disrate = 0.15
else:
    disrate = 0.10

discount = price * disrate
print("Discount = ", discount)
