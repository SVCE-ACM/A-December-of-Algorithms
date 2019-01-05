def generateSquare(n):

	magicSquare = [[0 for i in range(n)] for j in range(n)] 	i = n / 2

	j = n - 1

	num = 1

	while num <= (n * n): 

		if i == -1 and j == n: 

			j = n - 2

			i = 0

		else: 

			if j == n: 

				j = 0

			if i < 0: 

				i = n - 1			

		if magicSquare[int(i)][int(j)]:

			j = j - 2

			i = i + 1

			continue

		else: 

			magicSquare[int(i)][int(j)] = num 

			num = num + 1			

		j = j + 1

		i = i - 1 

	print ("Magic Squre for n =", n) 

	print ("Sum of each row or column",n * (n * n + 1) / 2, "\n") 

	

	for i in range(0, n): 

		for j in range(0, n): 

			print(magicSquare[i][j],end = '\t') 

			

			if j == n - 1: 

				print() 

n = int(input("Enter n for odd order: "))

generateSquare(n)
