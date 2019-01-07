def reverse(string):
	if(string == ''):
		return
	reverse(string[1:])
	print(string[0],end='')

s = input()
reverse(s)
