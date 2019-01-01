import itertools
def lex(li,s):
	li = list(itertools.permutations(li))
	li = [ ''.join(combos) for combos in li]
	li.sort()
	print(li)
	for i in range(len(li)):
		if li[i]==s:
			print(str(i+1)+' Position')
	
s = input('Enter input')
lex(list(s),s)