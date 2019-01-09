def isLucky(n):
    num=str(n)
    mid=len(str(n))//2
    sum1=0
    sum2=0
    for i in range(len(str(n))):
        if(i<mid):
            sum1+=int(num[i])
        else:
            sum2+=int(num[i])
    if(sum1==sum2):
        print("isLucky(n)=True")
    else:
        print("isLucky(n)=False")

n=int(input("Enter n:"))
isLucky(n)
    

