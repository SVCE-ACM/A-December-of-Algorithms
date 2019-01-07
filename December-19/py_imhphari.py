import string
def hash(s):
	s = list(s)
	for i in range(len(s)):
		s[i] = ord(s[i]) #ascii
	x = sum(s)
	print(x)
	
	print('Output:' + str(int(x/(len(s))**2)))
	
hash(input('enter string :'))
