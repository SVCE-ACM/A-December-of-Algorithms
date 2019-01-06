def islucky(num):
    len=0
    sum1=sum2=0
    temp=num
    while(temp!=0):
        len=len+1
        temp//=10
    #print(len)
    h=len//2
    for i in range(0,h):
        x=num%10
        sum1=sum1+x
        num//=10
    for j in range(h,len):
        y=num%10
        sum2=sum2+y
        num//=10
    if sum1==sum2:
        print("true")
    else:
        print("false")
    
num=int(input("Enter ticket number: "))
islucky(num)
