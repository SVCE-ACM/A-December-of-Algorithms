def identical_diagnoal(a,r,c):
	sr = r-2
	sc = 0
	for c in range(r):
		i = sr
		j = sc
		if a[i][j] == a[i+1][j+1]:
			i += 1
			j += 1
		else:
			print('Unidentical diagonals!')
			exit()
		if sr!= 0:
			sr -= 1
		else:
			sc += 1
	print('Identical diagonals!')





c = int(input('Enter number of rows of matrix 1'))
r = int(input('Enter number of coloumns of matrix 1'))
a = [ ['a' for i in range(0,c)] for j in range(0,r)]
print('Enter for matrix 1 : ')
for i in range(0,r):
	for j in range(0,c):
		a[i][j] = int(input('Enter element : '))
print(a)
identical_diagnol(a,r,c)
