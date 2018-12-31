def iddiag(a,r,c):
	sr = r-2
	sc = 0
	for c in range(r):
		i = sr
		j = sc
		if a[i][j] == a[i+1][j+1]:
			i += 1 
			j += 1
		else:
			print('Unidentical diagonals')
			exit()
		if sr!= 0:
			sr -= 1
		else: 
			sc += 1
	print('Identical diagonals')
			
				



c1 = int(input('Enter number of rows of m1'))
r1 = int(input('Enter number of coloumns of m1'))
m1 = [ ['a' for i in range(0,c1)] for j in range(0,r1)]
print('Enter matrix 1')
for i in range(0,r1):
	for j in range(0,c1):
		m1[i][j] = int(input('Enter element'))
print(m1)
iddiag(m1,r1,c1)