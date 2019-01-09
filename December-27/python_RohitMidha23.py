def vowel_square(a,r,c):
	i = 1
	j = 1
	itr = 2
	itc = 2
	f = 0
	while(1):
		while(itc<=c):
			count = 0
			for row in range(i-1,itr):
				for col in range(j-1,itc):
					if a[row][col] in ('a','e','i','o','u'):
						count += 1
						print('Tru')
					if count == 4:
						print(i-1,'-',j-1)
						f = 1
			j += 1
			itc = j + 1
		i += 1
		itr = i + 1
		j = 1
		itc = j+1
		if itr>r or itc>c:
			if f==0:
				print('Unavailable')
			break

c = int(input('Enter number of rows of matrix 1'))
r = int(input('Enter number of coloumns of matrix 1'))
a = [ ['a' for i in range(0,c)] for j in range(0,r)]
print('Enter for matrix 1 : ')
for i in range(0,r):
	for j in range(0,c):
		a[i][j] = int(input('Enter element : '))
print(a)
vowel_square(a,r,c)
