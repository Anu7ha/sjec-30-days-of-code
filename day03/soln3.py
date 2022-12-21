n=int(input('Enter the count: '))
s=[]
for i in range(n):
    s.append(int(input()))

avg=sum(s)/n

print("greater: ")
for i in s:
    if (avg<i):
        print(i)
        continue
    