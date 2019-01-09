def pascal(row):
	arr = [[0 for x in range(row)] for y in range(row)] 
	for i in range(0,row):
		arr[i][0] = 1
		arr[i][i]=1
	for i in range(row):
		for j in range(i+1):
			if arr[i][j] == 1:
				print(str(arr[i][j]),end='')
				
			else:
				arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
				print(str(arr[i][j]), end='')
		print('\t--> row',i,'\n')	

n = int(input('Enter number of rows :'))
pascal(n)
