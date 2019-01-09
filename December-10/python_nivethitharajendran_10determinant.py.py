import numpy
n=int(input("enter the no of rows"))
m=int(input("enter the no of colums"))
a=[[0]*n for i in range(0,n)]
for i in range(n):
  for j in range(m):
    a[i][j]=int(input())
det = numpy.linalg.det(a)
print("The determinant of the matrix is:",round(det))
