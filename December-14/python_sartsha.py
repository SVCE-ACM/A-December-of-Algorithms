s=input("Input: ").split()

word=s[0]
k = int(s[1])
print('Encoded output:',end = '')
for char in word:
	p = ord(char)+k
	if(p>122):
		p-=26
	print(chr(p),end='')
