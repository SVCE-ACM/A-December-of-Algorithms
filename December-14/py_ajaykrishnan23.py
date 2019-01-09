import string
def caesaren(s,a):
	li = []
	for char in s:
		x = ord(char)
		x = x + a
		char = chr(x)
		li.append(char)
	li =''.join(li)
	print(li)
	return li,a
def caesarde(s,a):
	li = []
	for char in s:
		x = ord(char)
		x = x - a
		char = chr(x)
		li.append(char)
	li =''.join(li)
	print(li)
print('Encryption')
li,a =caesaren(list(input('Enter String')),int(input('Enter number')))
print('decryption')
caesarde(list(li),a)