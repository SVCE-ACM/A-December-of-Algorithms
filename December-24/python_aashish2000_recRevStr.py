lst=input('Enter String: ')
def revstring(string):
	if len(string) == 0:
		return string
	else:
		return revstring(string[1:]) + string[0]

print (revstring(lst))