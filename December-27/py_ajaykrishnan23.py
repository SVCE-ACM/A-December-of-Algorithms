def vowsq(a,r,c):
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



r1 = int(input('Enter number of rows of m1'))
c1 = int(input('Enter number of coloumns of m1'))
m1 = [ ['a' for i in range(0,c1)] for j in range(0,r1)]
print('Enter matrix 1')
for i in range(0,r1):
	for j in range(0,c1):
		m1[i][j] = str(input('Enter element'))
vowsq(m1,r1,c1)