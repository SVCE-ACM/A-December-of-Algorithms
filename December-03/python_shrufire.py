def isLucky(n):
    a=n
    i=j=0
    while n>0:
        n/=10
        i=1
    sum1=sum2=0
    j=i
    while j>i/2: 
        sum1+=a%10
        a=a/10
        j=j-1
    while  j>0:
        sum2+=a%10
        a=a/10
        j=j-1    
    if sum1==sum2:
        return True
    else:
        return False
    
n=int(input('Enter your ticket number: '))
print(isLucky(n))
    
