# Dec 11
import numpy as np
# Enter with spaces
m, n = map(int, input("Enter number of rows and columns  ").split())
mat = np.zeros((m, n), dtype=int)
print("Enter the matrix: ")
for i in range(m):
    for j in range(n):
        mat[i, j] = int(input())
i, j = 0, 0
while i < m and j < n:
    for k in range(j, n):
        print(mat[i, k], end=" --> ")
    i += 1
    for k in range(i, m):
        print(mat[k, n-1], end=" --> ")
    n -= 1
    if i < m:
        for k in range(n-1, j-1, -1):
            print(mat[m-1, k], end=" --> ")
        m -= 1
    if j < n:
        for k in range(m-1, i-1, -1):
            print(mat[k, j], end=" --> ")
        j += 1
print("END")
# Sample I/O
# Enter number of rows and columns  3 3
# Enter the matrix:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 1 --> 2 --> 3 --> 6 --> 9 --> 8 --> 7 --> 4 --> 5 --> END
