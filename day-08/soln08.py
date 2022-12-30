from sympy import *
m=int(input("Enter the number m: "))
n=int(input("Enter the number n: "))
for i in range(m, n):
    if isprime(i):
        a=i
        b=nextprime(i)
        c=b-a-1
        if(b<n):
            print(f"{a} - {b} = {c} ")
