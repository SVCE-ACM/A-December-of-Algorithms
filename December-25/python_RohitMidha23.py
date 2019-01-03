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
sourcec = input("Enter Santa's source coordinates separated by ,"")
sourcec = sourcec.split(',')
sourcec = [int(x) for x in sourcec]
childc = input("Enter child's coordinates separated by ,"")
childc = childc.split(',')
childc = [int(x) for x in childc]
a[sourcec[1]][sourcec[0]] = 'S'
a[childc[1]][childc[0]] = 'K'
if childc[1]>sourcec[1]:
	santa(a,sourcec[1],sourcec[0],childc[1],childc[0],1)
else:
	santa(a,sourcec[1],sourcec[0],childc[1],childc[0],1)
