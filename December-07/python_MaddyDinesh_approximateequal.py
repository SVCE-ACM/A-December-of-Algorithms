from decimal import Decimal
n=int(input("1.without tolerance 2.with tolerance"))
if n==1:
  a=float(input("enter the 1st number"))
  b=float(input("enter the 2nd number"))
  x=round(a)
  y=round(b)
  if x==y:
    print("approximate equal")
  else:
    print("not equal")
else:
  a=Decimal(input("enter the 1st number"))
  b=Decimal(input("enter the 2nd number"))
  c=float(input("enter tolerance"))
  x=float(a-b)
  if x==c:
    print("approximate equal")
  else:
    print("not equal")