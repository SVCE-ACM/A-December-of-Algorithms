def lcm(n1,n2):
    if(n1>n2):
        a=n1
        b=n2
    else:
        a=n2
        b=n1
    rem=a%b
    while(rem!=0):
        a=b
        b=rem
        rem=a%b
    return((n1*n2)//b)

print("Input:",end=" ")
arr=list(map(int,input().split()))

l=arr[0]

for i in range(1,len(arr)):
    l=lcm(l,arr[i])

print("Output:",l)

    

    

