age = int(input("Enter Your Age="))
if age<= 13:
    print("you are a child")
elif age>13 and age<=19:
    print("you are a teenager")
elif age>20 and age<=59:
    print("you are an adult")
else:
    print("you are an old timer")