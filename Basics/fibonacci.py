num= int(input("Enter your number: "))
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(num):
    print(fibonacci(i))
#! dont know what it is
