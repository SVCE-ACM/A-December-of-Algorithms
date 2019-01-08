import itertools
s = input('Input :')
permu = list(itertools.permutations(s,len(s)))
permu = [ ''.join(combos) for combos in permu]
permu.sort()
for i in range(len(permu)):
	if permu[i]==s:
		print(permu[i]+" --> Match Found at Position "+str(i+1))
	else:
		print(permu[i])
