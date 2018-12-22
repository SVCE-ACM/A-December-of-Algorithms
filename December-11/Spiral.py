#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
import sys
import numpy as np

def spiral(mat,n):
    matrix1 =np.matrix(mat)
    print("THE ORGINAL MATRIX \n",matrix1)
    flag=0

    for i in range(0,n):
        if(flag==0):
            for j in range(0,n):
               print(mat[i][j],"-->",end=" ")
               flag=1
        elif(flag==1):
            for j in range(n-1,-1,-1):
                print(mat[i][j],"-->",end=" ")
            flag=0


def main():
     n = int(input("Enter the number of rows in a matrix:"))
     a = [[0 for x in range(n)] for y in range(n)]
     for i in range(n):
         for j in range(n):
             a[i][j] = int(input())
     spiral(a,n)
if __name__ == '__main__':
    main()
