def spiral(m,n,e):
    k=0
    l=0
    while k<m and l<n:
        for i in range(l,n):
            print(e[k][i],"-->",end="")
        k=k+1

        for i in range(k,m):
            print(e[i][n-1],"-->",end="")
        n=n-1

        if k<m:
            for i in range(n-1,(l-1),-1):
                print(a[m-1][i],"-->",end="")
            m=m-1
        if l<n:
            for i in range(m-1,(k-1),-1):
                print(a[i][l],"-->",end="")
            l=l+1
            
m =3
n=3
a = [ [1, 2, 3], 
      [4, 5, 6], 
      [7, 8, 9] ] 
spiral(m,n,a)

