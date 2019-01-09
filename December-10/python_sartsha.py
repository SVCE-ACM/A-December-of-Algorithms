import numpy as np
n = int(input('Enter order of matrix :'))
mat = [[0 for _ in range(n)] for i in range(n)]
det = np.linalg.det(mat)
print("Determinant =",det)
