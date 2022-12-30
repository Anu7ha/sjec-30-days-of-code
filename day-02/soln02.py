n=int(input('Enter the number of triangles: '))
side=[]
def small(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c

def medium(a,b,c):
    if((a<b and a>c) or (a>b and a<c)):
        return a
    elif((b<a and b>c) or (b>a and b<c)):
        return b
    else:
        return c

def large(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c  
for i in range(1,n+1):
    a=int(input('Enter 1st side: '))
    b=int(input('Enter 2st side: '))
    c=int(input('Enter 3rd side: '))
    print(a,b,c)
    if i%3==0:
        side.append(large(a,b,c))
    elif i%3==1:
         side.append(small(a,b,c))
    else:
         side.append(medium(a,b,c)) 
print(side)
    








     