def printable(a,b):
    for i in range(a,b+1):
        if i%3 == 0 :
            print ("Foo")
        elif(i%2==0) and (i%3!=0):
            print ("Bar")
        elif(i%2==1) and (i%3!=0):
            print ("Baz")
a=int(input('Enter 1st non negative number:'))
b=int(input('Enter 2nd non negative number:'))
printable(a,b)
