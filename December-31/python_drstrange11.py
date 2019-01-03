# Dec 31
import numpy as np


def ClosestCell2(s):
    l = []
    for num in s:
        val = np.array([int(x) for x in num])
        l.append(val)
    l = np.array(l)

    (m, n) = l.shape
    twos = []
    for i in range(m):
        for j in range(n):
            if l[i, j] == 1:
                loc = (i, j)
            elif l[i, j] == 2:
                twos.append((i, j))
    m = 1000
    for x, y in twos:
        m = min(m, abs(loc[0]-x)+abs(loc[1]-y))
        m = min(m, abs(loc[0]-(x+m))+abs(loc[1]-y))
        m = min(m, abs(loc[0]-x)+abs(loc[1]-(y+n)))
        m = min(m, abs(loc[0]-(x+m))+abs(loc[1]-(y+n)))
    print("Matrix :")
    print(l)
    return m


st = input("Enter the matrix as strings with spaces: ").split()
print("Output :", ClosestCell2(st))

# Sample I/O
# Enter the matrix as strings with spaces: 0000 2010 0000 2002
# Matrix :
# [[0 0 0 0]
#  [2 0 1 0]
#  [0 0 0 0]
#  [2 0 0 2]]
# Output : 2
