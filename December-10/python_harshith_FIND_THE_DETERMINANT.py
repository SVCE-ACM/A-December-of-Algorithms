import numpy as np
n=int(input("enter"))
a=[[0]*n for i in range(0,n)]
for i in range(n):
  for j in range(n):
    a[i][j]=int(input("enter"))
z=np.linalg.det(a)
print(int(round(z)))    
