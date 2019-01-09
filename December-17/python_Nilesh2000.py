import numpy as np


def magic_odd(N, M):  # Odd
    mat = np.zeros((N, N), dtype=int)
    i, j = 0, N//2
    num = 1
    while num <= N**2:
        mat[i, j] = num
        num += 1
        i = (i-1) % N
        j = (j+1) % N
        if mat[i, j]:
            j = (j-1) % N
            i = (i+2) % N
    return mat


n = int(input('Enter the Order: '))
m = int(input('Enter the Magic Sum: '))


def magic_four(N, M):  # Multiples of 4
    mat = np.zeros((N, N), dtype=int)
    i = 1
    for j in range(N):
        for k in range(N):
            mat[j, k] = i
            i += 1
    j = N-1
    for i in range(N):
        if i > j:
            break
        mat[i, i], mat[j, j] = mat[j, j], mat[i, i]
        j -= 1

    for i in range(N//2):
        mat[i, N-i-1], mat[N-i-1, i] = mat[N-i-1, i], mat[i, N-i-1]
    return mat


if n % 2 != 0:
    matrix = magic_odd(n, m)
else:
    matrix = magic_four(n, m)

print("All matrices")
print(matrix)
print("\n", np.transpose(matrix))
for i in range(n):
    matrix = np.flip(matrix, 1)
    print("\n", matrix)
    matrix = np.transpose(matrix)
    print("\n", matrix)
