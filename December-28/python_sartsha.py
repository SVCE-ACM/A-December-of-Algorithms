def check(matrix,m,n):
	for i in range(m-1):
		for j in range(n-1):
			if matrix[i][j] != matrix[i+1][j+1]:
				return False
	return True


m,n = map(int,input("Enter m and n: ").split())
mat = [[0 for i in range(n)] for j in range(m)]

print("Enter values of matrix in one line ")
inp = list(map(int,input().split()))
index=0
for i in range(m):
	for j in range(n):
		mat[i][j] = inp[index]
		index+=1
if(check(mat,m,n)):
	print('Identical diagonals')
else:
	print('Diagonals are non-identical')
