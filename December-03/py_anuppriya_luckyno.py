num=int(input("Enter the Ticket Number: "))
a=list(str(num))
s1=0
s2=0
i=0;
j=len(str(num))-1
while(i<j):
  i=i+1
  j=j-1
d=i
v=j
for c in range(0,d):
  s1=s1+int(a[c])
for e in range(v+1,len(a)):
  s2=s2+int(a[e])   
print("First half sum:",s1,"\nSecond half sum:",s2)
if(s1==s2):
  print("Its a Lucky number!")
else:
  print("Not a lucky number!")  












