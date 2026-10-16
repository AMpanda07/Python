
#? SUM OF THREE DIGIT

# n = int(input("enter a three digit number: "))
# temp = n
# sum = 0 
# while n > 0:
#     rem = n % 10
#     sum = sum + rem
#     n = n // 10
# print(sum)

# n=5 

#?Pattern
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

#? ARMSTRONG NUMBER
# n = 156 
# temp = n
# sum = 0
# digits = len(str(n))
# while n > 0:
#     rem = n % 10
#     sum = sum + rem ** digits
#     n = n // 10
# if sum == temp:
#     print(temp, "is an Armstrong number")
# else:
#     print(temp, "is not an Armstrong number")

#? PALINDROME 

n = 121
temp = n
rev = 0
while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
if rev == temp:
    print(temp, "is a palindrome")
else:
    print(temp, "is not a palindrome")

#?prime in range 

n = int(input("Enter a range: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i,end=" ")