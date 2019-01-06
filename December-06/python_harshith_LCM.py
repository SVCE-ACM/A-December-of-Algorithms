def GCD(x, y):
   while(y):
       x, y = y, x % y

   return x
a=int(input("Enter the total number of numbers"))   
num = []
for i in range(0,a):
    num.append(int(input('Enter the number: ')))
lcm=num[0]
for i in num:
  lcm=lcm*i//GCD(lcm,i)
print(lcm)
