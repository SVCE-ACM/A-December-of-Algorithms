import inflect
p=inflect.engine()
a=input("Enter the first parameter")
z=a[1]
b=input("Enter the second parameter")
if b.isnumeric() :
  if b=="1" or b=="-1":
    if a[-1]=="s":
      print(p.plural(a))
    else:
      print(a)  
  else:
    if a[-1]=="s":
      print(a)
    else:
      print(p.plural(a)) 
else:
  if a[1]==b[1]:
    if a[-1]=="s":
     b=p.plural(a)
     print("SINGULAR:",b)
     print("PLURAL:",a)
    else:
     b=p.plural(a)
     print("SINGULAR:",a)
     print("PLURAL:",b)  
  else:
    print("INVALID INPUT")