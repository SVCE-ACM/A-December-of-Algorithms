#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

def spiralPrint(m, n, a):
    k = 0
    l = 0
    while (k < m and l < n):


        for i in range(l, n):
            print(a[k][i],"-->", end=" ")

        k += 1


        for i in range(k, m):
            print(a[i][n - 1],"-->", end=" ")

        n -= 1
        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i],"-->", end=" ")

            m -= 1
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l],"-->", end=" ")

            l += 1
def main():
  n = int(input("Enter the number of rows/columns in a matrix:"))
  a = [[0 for x in range (n)] for y in range(n)]
  for i in range (n):
    for j in range(n):
        a[i][j]=int(input())

  spiralPrint(n,n,a)
if __name__ == '__main__':
    main()



