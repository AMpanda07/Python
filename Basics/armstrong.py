num = int(input("Enter a number: "))
def armstrong(num):
    n=len(str(num))
    temp = num
    sum=0
    while num>0:
        rem = num %10
        sum = rem**n + sum
        num = num//10
    if sum==temp:
        return 1
    else:
        return 0
if armstrong(num):
    print(num,"is armstrong")
else:
    print(num,"is not armstrong")