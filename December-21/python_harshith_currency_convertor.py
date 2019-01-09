import pandas as pd
data=pd.read_excel("EXCHANGE RATES.xlsx")
a=input("From country")
c=int(input("Enter the amount to be transferred"))
b=input("To country")
d=data[data.LOCATION==a]
e=data[data.LOCATION==b]
f=float(c / float (d.VALUE))*float (e.VALUE)
print(c,"(",a,")",f,"(",b,")")
