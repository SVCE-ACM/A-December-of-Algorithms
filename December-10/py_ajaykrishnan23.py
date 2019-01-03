import numpy
def determinant(m1):
	print (numpy.linalg.det(m1))

r1 = int(input('Enter number of rows of m1'))
c1 = int(input('Enter number of coloumns of m1'))

if c1 != r1:
	print('Determinant not possible to find')
	exit()
else:
	m1 = [ [0 for i in range(0,c1)] for j in range(0,r1)]
	print('Enter matrix 1')
	for i in range(0,r1):
		for j in range(0,c1):
			m1[i][j] = int(input('Enter element'))
determinant(m1)