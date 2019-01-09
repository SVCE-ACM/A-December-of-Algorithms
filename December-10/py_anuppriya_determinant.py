import numpy as np

m=int(input("Enter the no of rows:"))
n=int(input("Enter  the no of columns:"))

mat=[]
for i in range(0,n):
    mat.append([])
for i in range(0,m):
    for j in range(0,n):
        mat[i].append(j)
        mat[i][j]=0
for i in range(0,m):
    for j in range(0,n):
        mat[i][j]=int(input())
print(mat)

print(np.linalg.det(mat))
