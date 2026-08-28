
#? problem 5.6

#!

n = int(input("Enter a number: "))
if n > 0:
    flag = True
    print(n*n)
elif n < 0:
    flag = True
    print(n*n*n)
else:
    pass