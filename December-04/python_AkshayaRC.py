n=int(input("enter nth no.to be found: "))
f0=0
f1=1
for i in range(2,n):
    f2=f0+f1
    f0=f1
    f1=f2
print(n,"th number in the series is ",f2)    
    
