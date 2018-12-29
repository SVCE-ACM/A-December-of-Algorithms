def spiralPrint(m, n, a) : 
    k = 0; l = 0



    while (k < m and l < n) : 

        for i in range(l, n) : 
            print(a[k][i], end = " ") 

        k += 1

        for i in range(k, m) : 
            print(a[i][n - 1], end = " ") 

        n -= 1

        if ( k < m) : 

            for i in range(n - 1, (l - 1), -1) : 
                print(a[m - 1][i], end = " ") 

            m -= 1

        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(a[i][l], end = " ") 

            l += 1

aR=int(input("ENTER THE NUMBER OF ROWS"))
aC=int(input("ENTER THE NUMBER OD COLUMNS"))
a=[[0]*aC for i in range(aR)]
for i in range(aR):
  for j in range(aC):
    a[i][j]=int(input("ENTER"))


spiralPrint(aR, aC, a) 