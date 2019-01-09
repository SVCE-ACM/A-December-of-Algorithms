import validators
def isurl(s):
	if validators.url(s):
		print('Yes')
	else:
		print('no')
		
s = input('Enter url')
isurl(s)