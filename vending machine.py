print("Welcome to riri's vending machine")
print("Item:           price:       code:")
print("Coke            $3.0           1 ")
print("Coffee          $2.50          2 ")
print("Water           $0.50          3 ")
print("Gatorade        $1.50          4 ")
print("Cobra           $3.25          5 ")

user = int(input("enter your order here:"))

if user == 1:
    price = float (3.0)
    print("You have selected Coke. Please pay $3.0")

elif user == 2:
    price = float(2.50)
    print("You have selected Coffee. Please pay $2.50")

elif user == 3:
    price = float(0.50)
    print("You have selected Water. Please pay $0.50")

elif user == 4:
    price = float(1.50)
    print("You have selected Gatorade. Please pay $1.50")

elif user == 5:
    price = float(3.25)
    print("You have selected Cobra. Please pay $3.25")

while True:
    pay = float(input("pay here: $"))

    if pay < price:
        print("amount is not enough")
    else:
        break
  
change = float(pay - price)
print(f"Here is your change:${change}")

print("thank you for coming!")

