#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
import numpy.linalg as m
import numpy as np

def deter(mat):
    matrix1 =np.matrix(mat)
    print("THE ORGINAL MATRIX \n",matrix1)
    print("THE DETERMINANT \n",m.det(matrix1))

def main():
     n = int(input("Enter the number of rows in a matrix"))
     a = [[0 for x in range(n)] for y in range(n)]
     for i in range(n):
         for j in range(n):
             a[i][j] = int(input())
     deter(a)
if __name__ == '__main__':
    main()
