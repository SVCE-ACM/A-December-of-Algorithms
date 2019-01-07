import numpy as np
mat = np.full((11, 11), '*')
y1, x1 = map(int, input("Santa's Location: ").split())
mat[x1, y1] = 'S'
y2, x2 = map(int, input("Child's Location: ").split())
mat[x2, y2] = 'K'
for i in range(x1+1, x2+1):
    mat[i, y1] = ' '
for i in range(y1+1, y2):
    mat[x2, i] = ' '
for i in range(10):
    for j in range(10):
        print(mat[i, j], end=" ")
    print()
