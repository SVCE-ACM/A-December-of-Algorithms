def fact(n):
    if n==0:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact    

row=int(input("enter no.of rows: "))
lis=[]
c=0
for n in range(row+1):
    print("\n")
    for r in range(n,row):
       print("  ",end="")
    for r in range(0,n+1):
        num=fact(n)//(fact(r)*fact(n-r))
        print(num,end="   ")
    for r in range(n,n+1):
        n=row
        num=fact(n)//(fact(r)*fact(n-r))
        lis.append(num)
print("\n\nPolynomial: ")
for i in range(len(lis)):
    print("(",lis[i],"x^",row,"y^",c,")",end=" ",sep="")
    if i!=len(lis)-1:
        print("+",end="")
    c+=1
    row-=1
