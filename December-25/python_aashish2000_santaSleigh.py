y1,x1=(input("Santa's Location: ").split(','))
y1=int(y1[1:])
x1=int(x1[:-1])

y2,x2=(input("Child's Location: ").split(','))
y2=int(y2[1:])
x2=int(x2[:-1])

mat=[['*', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
for i in range(10):
	mat.append([i, '*', '*','*','*','*','*','*','*','*','*'])
mat[x1+1][y1+1]='S'
mat[x2+1][y2+1]="K"

if (x1==x2) and (y1!=y2):
	if y2>y1:
		for i in range(y1+2, y2+1):
			mat[x1+1][i]=' '
	else:
		for i in range(y2+2, y1+1):
			mat[x1+1][i]=' '
elif (x1!=x2) and (y1==y2):
	if x2>x1:
		for i in range(x1+2, x2+1):
			mat[i][y1+1]=' '
	else:
		for i in range(x2+2, x1+1):
			mat[i][y1+1]=' '
else:
	if y2>y1:
		for i in range(y1+2, y2+1):
			mat[x1+1][i]=' '
	else:
		for i in range(y2+2, y1+1):
			mat[x1+1][i]=' '
	if x2>x1:
		for i in range(x1+2, x2+1):
			mat[i][y2+1]=' '
	else:
		for i in range(x2+2, x1+1):
			mat[i][y2+1]=' '
	mat[x1+1][y2+1]=' '
	 

for i in mat:
	print (" ".join(map(str,i)))
