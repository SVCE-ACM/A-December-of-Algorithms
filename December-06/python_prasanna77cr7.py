def gcd(n1,n2):
  if n2!=0:
    return gcd(n2,n1%n2)
  else:
    return n1
n=int(input("enter the total no of terms"))
a=[]
for i in range(n):
  a.append(int(input()))
lcm=a[0]
for i in a:
  lcm=lcm*i//gcd(lcm,i)
print("the lcm is",lcm) 
