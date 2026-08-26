
#? Problem 5.1

#! While Purchasing certain items, a discount of 10% is offered if the quantity purchased is more then 1000. if quantity and price per item are input through the keyboard , write a program to calculate the total expenses.

quantity = int(input("Enter the quantity purchased: "))
price = int(input("Enter the price per item: "))

t = price*quantity

if quantity > 1000:
    discount = 0.1
else:
    discount = 0

Total = t - (discount * t)

print("Your total expenses are: ", Total)