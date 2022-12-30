m=int(input("Enter the rows: "))
n=int(input("Enter the columns: "))

if(m*n%3==0 and m!=n and ((m%2==0  and n%3==0)or(m%3==0 and n%2==0))):
    print("yes")
elif(m==n and m!=3 and m*n%3==0 and (m%3==0 and n%2==0)):
    print("yes")
else:
    print("No")
