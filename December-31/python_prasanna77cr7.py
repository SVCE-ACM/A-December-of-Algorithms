def cc(a):
	r = len(a)
	c = len(a[0])
	s = 100
	for i in range(r):
		for j in range(c):
			if a[i][j] == 1:
				break
		if a[i][j] ==1:
			break
	for k in range(r):
		for l in range(c):
			if a[k][l]==2:
				print(i,j,k,l)
				x = abs(i-k)+abs(j-l)
				if x<s:
					s = x
					print(s)
	if s>0:
		print(s)
	else:
		print(0)
r1 = int(input('Enter number of rows:'))
c1 = int(input('Enter number of columns:'))
m= [ [0 for i in range(0,c1)] for j in range(0,r1)]
print('Enter matrix')
for i in range(r1):
	for j in range(c1):
		m[i][j] = int(input('Enter element'))
cc(m)
