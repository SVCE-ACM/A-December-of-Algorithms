def calc(n1, n2): 
    if(n1>n2): 
        num = n1 
        den = n2
    else: 
        num = n2 
        den = n1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(n1 * n2)/int(gcd)) 
    return lcm 

s=int(input("Enter size:"))
a=[0]*s
print("Input numbers: ")
for i in range(s):
  a[i]=int(input())
print("List: ",a)

  
n1 = a[0] 
n2 = a[1] 
lcm =calc(n1,n2) 
  
for i in range(2, len(a)): 
    lcm =calc(lcm, a[i]) 
print("LCM is: ",lcm) 
  






















