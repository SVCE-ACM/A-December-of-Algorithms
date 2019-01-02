import pandas as pd
data=pd.read_excel("Book1.xlsx")
a=input("enter the form country")
b=input("enter the to country")
c=int(input("enter the amount to be transferred"))
d=data[data.LOCATION==a]
e=data[data.LOCATION==b]
f=float(c/ float(d.VALUE))*float(e.value)
print("amount in")
print(b)
print("is")
print(f)
