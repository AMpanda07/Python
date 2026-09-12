
s = input("Enter your string: ")

split_string = s.split()

# print("The split string is: ", split_string)
length = len(split_string)
# print("The length of the split string is: ", length)

for i in range(length,0,-1):
    print(split_string[i-1], end=" ")
