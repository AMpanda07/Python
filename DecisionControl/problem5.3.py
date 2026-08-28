
#? problem 5.3

#!

percentage = int(input("Enter the percentage: "))

if percentage >= 60:
    print("First division")
elif percentage >= 50 and percentage < 60:
    print("Second division")
elif percentage >= 40 and percentage <50:
    print("Third division")
else:
    print("Fail")