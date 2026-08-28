
#? Problem 5.2

#! calculate

salary = float(input("Enter your salary: "))
if salary <1500:
     HRA = 0.10 * salary
     DA = 0.90 * salary
else:
    HRA = 500 
    DA = 0.98 * salary

Total = HRA + DA + salary
print("Total salary:", Total)