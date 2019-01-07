def spiralPrint(m, n, a):
    k = 0
    l = 0
    while (k < m and l < n):
        for i in range(l, n):
            print(a[k][i], end=" ")
        k += 1

        for i in range(k, m):
            print(a[i][n - 1], end=" ")
        n -= 1

        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
            m -= 1

        if (l < n):
            for i in range(m-1,k-1,-1):
                print(a[i][l], end=" ")
            l += 1

n,m = map(int,input("Enter number of rows and columns :").split())
a = [[0 for x in range (m)] for y in range(n)]
for i in range (n):
    for j in range(m):
        a[i][j]=int(input())
print('Matrix')
for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print()
print('Spiral Form')
spiralPrint(n,m,a)
