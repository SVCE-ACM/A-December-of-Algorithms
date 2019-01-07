import numpy as np

n=int(input("Matrix Size:"))
print("Input Array(X):")
mat=[]
for i in range(n):
    row=list(map(int,input().split()))
    mat.append(row)

print("determinant(X):")
a=np.array(mat)
print(np.linalg.det(a))



