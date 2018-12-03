import inflect
p=inflect.engine()
a=input("Enter the first parameter")
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
     d=p.plural(a)
     print("SINGULAR:",d)
     print("PLURAL:",a)
    else:
     d=p.plural(a)
     print("SINGULAR:",a)
     print("PLURAL:",d)  
  else:
    print("INVALID INPUT")
