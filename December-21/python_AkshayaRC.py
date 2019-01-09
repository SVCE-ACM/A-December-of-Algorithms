##import re     
##def cc(fromC,toC,amt):
##    f=open('rates.html','r')
##    fromC=fromC.lower().replace(" ","")
##    toC=toC.lower().replace(" ","")
##    file=f.read().lower().replace(" ","")
##    l=re.findall(r'<td>(\w+)</td><td>(\d.*)</td>',file)
##    for loc,val in l:
##        if fromC==loc:
##            fro=float(val)
##        if toC==loc:
##            to=float(val)
##    exc=(amt/fro)*to       
##    print(amt,"(",fromC,") = ",exc," (",toC,")")
##    #print(exc)
##
##fromC=input("From country: ")
##amt=int(input("Currency i have: "))
##toC=input("To country: ")
##cc(fromC,toC,amt)
import csv
with open("Dec21-Exchange_Rates.csv","r") as csvfile:
    reader=csv.DictReader(csvfile)
    fromC=input("From country: ")
    amt=int(input("Currency i have: "))
    toC=input("To country: ")
    #cc(fromC,toC,amt)
    for row in reader:
        if row['LOCATION']==fromC:
            fro=float(row['VALUE'])
        if row['LOCATION']==toC:
            to=float(row['VALUE'])
    exc=(amt/fro)*to       
    print(amt,"(",fromC,") = ",exc," (",toC,")")
