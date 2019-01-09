#getting the numbers for which lcm has to be found
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
#calculating gcd
for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        gcd=i
#calculating lcm        
lcm=int((n1*n2)/gcd)
#displaying the output
print(lcm)
