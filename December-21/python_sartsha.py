from csv import reader
rates = {}
with open('Dec21-Exchange_Rates.csv') as f:
	r = reader(f)
	for row in r:
		rates[row[0]] = row[1]

frm = input("From Country: ")
n = float(input("Currency I have: "))
to = input("To Country ")
converted = n*float(rates[to])/float(rates[frm])
print(n,'('+frm+') =',round(converted,4),'('+to+')')
