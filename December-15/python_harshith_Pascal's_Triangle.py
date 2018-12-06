x=int(input("Enter the number"))
a=[1]
b=[1,1]
c=0
while c<x:
    print(a)
    a,b=b,[1]+[sum(p) for p in zip(b,b[1:])]+[1]
    c+=1
