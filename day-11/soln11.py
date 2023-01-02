def circle(r):
    return 3.14*r*r
def squ(a):
    return a*a
def tri(t):
    return(1.73*t*t/4)
def rect(l,b):
    return(l*b)

m=circle(int(input("Enter r:")))

n=squ(int(input("Enter a:")))

o=tri(int(input("Enter t:")))

l=int(input("Enter l:"))
b=int(input("Enter b:"))
p=rect(l,b)

s={m: "Circle",
    n: "Square",
    o: "triangle",
    p: "Rectangle"}

key_list=list(s.keys())
print(key_list)

key_list.sort(reverse=True)


for key in key_list:
    print(s[key])



