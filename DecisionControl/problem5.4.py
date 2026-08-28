
#? problem 5.4

#!

martial_status = input("Enter the martial status (single/married): ")
sex = input("Enter the sex (male/female): ")
age = int(input("Enter your age: "))

if (martial_status == "married") :
    print("Eligible for insurance")
elif (martial_status == "single" and sex == "male" and age > 30) :
    print("Eligible for insurance")
elif (martial_status == "single" and sex == "female" and age > 25) :
    print("Eligible for insurance")
else :
    print("Not eligible for insurance")