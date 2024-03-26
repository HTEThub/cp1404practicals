totalPrice = 0
DISCOUNT = 0.10
numOfItems = int(input("How many items are you buying?: "))

while numOfItems < 0:
    print("Invalid number of items!")
    numOfItems = int(input("How many items are you buying?: "))

for eachItem in range(1, numOfItems+1):
    print("For Item #", eachItem, sep="")
    price = float(input("Item price?: $"))
    while price < 0:
        print("Invalid price")
        price = float(input("Item price?: $"))
    totalPrice = totalPrice + price
    print("Total Price: $", totalPrice, sep="")
    print()

if totalPrice > 100:
    discountedPrice = totalPrice * DISCOUNT
    totalPrice = totalPrice - discountedPrice
    print("You got 10% discount!")
print(f"Your final price is: ${totalPrice:.2f}")
print("Thank you for shopping!")
