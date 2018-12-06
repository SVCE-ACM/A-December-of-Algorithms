x=input("Enter the input string")
y=int(input("Enter the number"))
for i in x:
  print(chr(ord(i)+y),end=" "),
