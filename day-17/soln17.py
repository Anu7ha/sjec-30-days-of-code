e=int(input("ele:"))
i=input()
a=list(map(int,i.split()))
n=[]
for i in range (1,e):
    if a[i-1]!=a[i]:
        n.append(a[i-1])
n.append(a[-1])

listToStr = ' '.join(map(str, n))
print(listToStr)
