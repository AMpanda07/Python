
#* Functions and recursion
n=int(input("enter count down: "))

def bomb(n):
    if not n:
        print("A")
    else:
        for n in range(n,0,-1):
            print(n)
bomb(n)