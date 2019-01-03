import numpy
def santa(a,sr,sc,cr,cc,sd):

	if sd == -1:
		while(sc != cc):
			sc = sc - 1
		print(a)
		
		
	elif sd == 1:
		while(sc != cc):
			sc = sc+ 1
			a[sr][sc] = ' '
		print(a)
	
	a =numpy.transpose(a)
	print(a)
	if sc == cc and sr == cr:
		a[cc][cr] = 'K'
		for row in range(10):
			for col in range(10):
				print(a[row][col],end=' ')
			print('\n')
	else:
		if sr > cr:
			santa(a,sc,sr,cc,cr,-1)
		else:
			santa(a,sc,sr,cc,cr,1)
		
		
a = [['*' for x in range(10)] for y in range(10)]
sl = input('enter Santa\'s source coordinates separated by ,')
sl = sl.split(',')
sl = [int(x) for x in sl]
cl = input('enter child\'s coordinates separated by ,')
cl = cl.split(',')
cl = [int(x) for x in cl]
a[sl[1]][sl[0]] = 'S'
a[cl[1]][cl[0]] = 'K'
if cl[1]>sl[1]:
	santa(a,sl[1],sl[0],cl[1],cl[0],1)
else:
	santa(a,sl[1],sl[0],cl[1],cl[0],1)