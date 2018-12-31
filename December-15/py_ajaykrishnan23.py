def pascal(row):
	a = [[0 for x in range(row)] for y in range(row)] 
	for i in range(0,row):
		a[i][0] = 1
		a[i][i]=1
	for i in range(0,row):
		for j in range(i+1):
			if a[i][j] == 1:
				print(str(a[i][j]),end='')
				
			else:
				a[i][j] = a[i-1][j-1]+a[i-1][j]
				print(str(a[i][j]), end='')
		print('\n')	

pascal(int(input('Enter number rows')))
			