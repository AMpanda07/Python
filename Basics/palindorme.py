n = int(input("Enter your number: "))
temp = n
reverse=0
while n>0:
    digit = n%10
    reverse = reverse*10 + digit
    n//=10
print("reverse number is: ",reverse)
if reverse == temp:
    print("palindrome")
else:
    print("not palindrome")
