def closestcell2(a):
	r = len(a)
	c = len(a[0])
	sol = 100
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
				smol = abs(i-k)+abs(j-l)
				if smol<sol:
					sol = smol
					print(sol)
					
	if sol>0:
		print(sol)
	else:
		print(0)
	
r1 = int(input('Enter number of rows of m1'))
c1 = int(input('Enter number of coloumns of m1'))
m1 = [ [0 for i in range(0,c1)] for j in range(0,r1)]
print('Enter matrix 1')
for i in range(r1):
	for j in range(c1):
		m1[i][j] = int(input('Enter element'))
closestcell2(m1)