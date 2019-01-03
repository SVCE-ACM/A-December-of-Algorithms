# Dec 28
import numpy as np
# Enter with spaces
m, n = map(int, input("Enter number of rows and columns  ").split())
flag = True
mat = np.zeros((m, n), dtype=int)
for i in range(m):
    for j in range(n):
        mat[i, j] = int(input())
for i in range(m-1):
    for j in range(n-1):
        if mat[i, j] != mat[i+1, j+1]:
            flag = False
            break
    if not flag:
        break
print(mat)
if flag:
    print("Identical diagonals")
else:
    print("Diagonals are non-identical")

# SAMPLE I/O
# Enter number of rows and columns  3 4
# 7
# 4
# 6
# 8
# 1
# 7
# 4
# 6
# 9
# 1
# 7
# 4
# [[7 4 6 8]
#  [1 7 4 6]
#  [9 1 7 4]]
# Identical diagonals
