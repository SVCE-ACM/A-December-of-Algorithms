import validators
def IsURL(url):
	if (validators.url(url) == True):
		return True
	else:
		return False
print(IsURL(input('Enter URL :')))
