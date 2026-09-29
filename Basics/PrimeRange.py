start=int(input("Enter start value: "))
end=int(input("Enter end value: "))
def prime(s,e):
    count = 0
    for num in range(s,e+1):
        for i in range(1,num+1):
            if count<=2:
                print(num,"is prime")
prime(start,end)