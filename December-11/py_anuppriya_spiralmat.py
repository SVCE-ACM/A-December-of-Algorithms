
def SpiralPrinting(a,m,n):



    
    t = 0
    b = m-1
    l = 0
    r = n - 1
    dr = 0
    
    """ 
    t: top of the matrix
    b: botom of the matrix
    l: left of the matrix
    r: Right of yhe matrix
    dr: printing direction
    m: Number of rows in the matrix
    n: Number of Columns in the matrix
    
    """
    
    while (t <= b and l <=r):
        
        if dr ==0:
            for i in range(l,r+1):
                print (a[t][i], end=" ")
            t +=1
            dr = 1
            
        elif dr ==1:
            for i in range(t,b+1):
                print (a[i][r], end=" ")
            r -=1 
            dr = 2
            
        elif dr ==2:
            for i in range(r,l-1,-1):
                print (a[b][i], end=" ")
            b -=1
            dr = 3
            
        elif dr ==3:
            for i in range(b,t-1,-1):
                print (a[i][l], end=" ")
            l +=1
            dr = 0



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


SpiralPrinting(mat,m,n)
