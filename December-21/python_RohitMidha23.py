import numpy as np 
import pandas as pd 
import csv
df = pd.read_csv('/Users/rohit/A-December-of-Algorithms/src/docs/Dec21-Exchange_Rates.csv',encoding = "ISO-8859-1")
fromc = input("From country : ")
amt = float(input("Currency you have : "))
toc = input("To country : ")

# csv to Dictionary Convert
with open('/Users/rohit/A-December-of-Algorithms/src/docs/Dec21-Exchange_Rates.csv', mode='r',encoding = "ISO-8859-1") as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}

fvalue = mydict[fromc]
tvalue = mydict[toc]
usd = amt/float(fvalue) 
finalvalue = usd * float(tvalue)
print(str(amt)+" ("+fromc+")"+" = "+str(finalvalue)+" ("+toc+")")