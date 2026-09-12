
#? write a PP to find a substring inside a string

string = input("Enter string: ")
print("String is: ",string)
substring =input("Enter substring: ")

if substring in string:
    print("Substring '" , substring , "' found in the string.")
else:
    print("Substring '" , substring , "' not found in the string.")