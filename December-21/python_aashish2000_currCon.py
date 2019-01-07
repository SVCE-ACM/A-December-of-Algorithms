coun1=str(input("From Country: "))
bucks=float(input("Currency I have: "))
coun2=str(input("To Country: "))
import csv
conv_coun1=None
conv_coun2=None
with open('Dec21-Exchange_Rates.csv', encoding="utf8", errors="ignore") as csvfile:
	reader=csv.reader(csvfile)
	for row in reader:
		if row[0]==coun1:
			conv_coun1=float(row[1])
		elif row[0]==coun2:
			conv_coun2=float(row[1])
		if (conv_coun1!=None) and (conv_coun2!=None):
			break
ans=(bucks*conv_coun2)/(conv_coun1)
print ('{} ({}) = {} ({})'.format(bucks, coun1, ans, coun2))