
#? Problem 6.1

#! 

a = 1

while a<=3:
    p = float(input("Value of price: "))
    n = int(input("Value of n: "))
    r = float(input("Value of r: "))
    
    SI = p*n*r / 100
    print("Simple Interest is: ", SI)
    a+=1