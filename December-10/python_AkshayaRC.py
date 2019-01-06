import sys
n=int(input("enter order of matrix (n*n)"))
if not(n==3 or  n==2):
    print("Enter order 2 or 3")
    sys.exit()
a=[[0]*n for i in range(n)]
print("enter matrix elements")
for i in range(0,n):
    for j in range(0,n):
        a[i][j]=int(input())
if n==2:
    det=(a[0][0]*a[1][1])-(a[0][1]*a[1][0])
elif n==3:
    det=(a[0][0]*((a[1][1]*a[2][2])-(a[1][2]*a[2][1])))-(a[0][1]*((a[1][0]*a[2][2])-(a[2][0]*a[1][2])))+(a[0][2]*((a[1][0]*a[2][1])-(a[2][0]*a[1][1])))
print("determinant: ",det)    
