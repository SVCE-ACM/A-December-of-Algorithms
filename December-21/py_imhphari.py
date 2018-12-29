import csv

with open('Dec21-Exchange_Rates.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    country=input("From Country: ")
    curr=int(input("Currency I have: "))
    to=input("To Country: ")
    for row in reader:
        if(row['LOCATION']=='India'):
            val=float(row['VALUE'])
            
        if(row['LOCATION']==to):
            va=float((row['VALUE']))
            
    c=((va*curr/val))
    print(c)
    
    print(curr, " ( ",country,")  = ",c," (",to,")")
