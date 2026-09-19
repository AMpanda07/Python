
#?wpp to find minimum of three numbers


def minimum():
    a =int(input("Enter number a: "))
    b =int(input("Enter number b: "))
    c =int(input("Enter number c: "))
    if a<c and a<b:
        print(a, " is minimum")
    elif b<a and b<c:
        print(b, " is minimum")
    else:
        print(c, " is minimum")

minimum()