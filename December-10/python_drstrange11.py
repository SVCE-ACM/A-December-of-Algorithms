# Dec 10
import numpy as np

l = []
n = int(input("Enter number of rows: "))
print("Enter the matrix row-wise with spaces")
while n > 0:
    l.append(list(map(int, input().split())))
    n -= 1
print(f"Determinant={np.linalg.det(l).round()}")

# Sample Input
# Enter number of rows: 3
# Enter the matrix row-wise with spaces
# 4 9 2
# 3 5 7
# 8 1 6
# Determinant=360.0
