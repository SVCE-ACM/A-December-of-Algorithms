x=(input("Enter the number:"))
l=int(len(x)/2)
a=int(str(x)[:l])
a=str(a)
a1=[]
for i in a:
  a1.append(int(i))
  a2=sum(a1)
b=int(str(x[l:len(x)]))
b=str(b)
b1=[]
for i in b:
  b1.append(int(i))
  b2=sum(b1)
if a2==b2:
  print("Lucky")  
else:
  print("Unlucky")  
