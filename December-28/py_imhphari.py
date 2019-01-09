m=int(input("enter no.of rows :"))
n=int(input("enter no.of columns :"))
flag=[]
matrix=[[0 for j in range(n)] for i in range(m)]
print("Enter matrix elements")
for i in range(0,m):
    for j in range(0,n):
        matrix[i][j]=int(input())
print("Given input matrix: ")
for i in range(m):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print("",sep="\n")    
for k in range(m-1,-1,-1):
    i=k
    j=0
    while(i<=m-1):
        if i+1<=m-1:
           if matrix[i][j]==matrix[i+1][j+1]:
               flag.append("1")
           else:
               flag.append("-1")
        i+=1
        j+=1
for k in range(1,n):
      i=0
      j=k
      while(j<=n-1):
          if j+1<=n-1:
            if matrix[i][j]==matrix[i+1][j+1]:
               flag.append("1")
            else:
               flag.append("-1")
          i+=1
          j+=1
if "-1" in flag:
    print("\nDiagonals are not identical")
else:
    print("\nIdentical diagonals")
