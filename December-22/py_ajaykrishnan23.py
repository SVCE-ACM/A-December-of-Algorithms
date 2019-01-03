import sys
import re 
import operator
def storewords(s):
	dict = {}
	s = s.split(' ')
	#print(s)
	for word in s:
		word = word.lower()
		if word not in dict:
			dict[word] = 1
		else:
			dict[word] += 1
	fname = input('enter filename')
	dict = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
	f = open(fname+'.txt',"w+")
	for entry in dict:
		f.writelines(str(entry[0])+' : ' + str(entry[1]) + '\n')
	return dict

def print_words(string):
	dict=storewords(string)
	for k in range(0,len(dict)):
		print (dict[k][0], dict[k][1])

def print_top(string):
	dict=storewords(string)
	#print(dict)
	for k in range(0,21):
		print (str(dict[k][0]), str(dict[k][1]))
		
f = input('Enter string')
#dict = storewords(f)
choice = int(input('1.Print all occurences.\n2.Print top 20.(Only in cases with 20+ unique strings'))
if choice == 2:
	print_top(f)
elif choice == 1:
	print_words(f)
else:
	print('Choice not present in the menu.')
	exit()