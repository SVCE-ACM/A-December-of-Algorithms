#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

import csv
def convert():
	f = open('Dec21-Exchange_Rates.csv',"r")
	reader = csv.reader(f)
	dict = {}
	for row in reader:
		dict[row[0]] = row[1]
	fromc = input('Enter country')
	toc = input('Enter country to which to be converted')
	amt = float(input('enter the amount to be converted'))
	print(dict[fromc])
	amt_new = amt/float(dict[fromc])
	print(dict[toc])
	amt_new = amt_new*float(dict[toc])
	print(str(amt)+'('+'fromc) = '+ str(amt_new) + '(Toc)')
	
def showall4country():
	f = open('Dec21-Exchange_Rates.csv',"r")
	reader = csv.reader(f)
	dict = {}
	for row in reader:
		dict[row[0]] = row[1]
	fromc = input('Enter country whose value in each other country is to be found')
	del dict['LOCATION']
	for entry in dict:
		print(entry +' : '+ str(float(dict[entry])/float(dict[fromc])))

ch = int(input('1->Currency converter\n2->Value of that country currency in the other countries'))
if ch==1:
	convert()
else:
	showall4country()
		
