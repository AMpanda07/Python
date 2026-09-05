
#! Date:- 05/09/2026

#? Q1 

nl = int(input("Enter lower limit: "))
nr = int(input("Enter upper limit: "))
sum = 0
for n in range(nl,nr):
    if n%2==1:
        sum +=n
print("sum of all the odd numbers are: ", sum)
