#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

import numpy as np
temp=0
numd=0
matrix=[]
new=[]
row=int(input("ENTER THE NO. OF ROWS:"))
col=int(input("ENTER THE NO. OF COLS:"))
print("//THE FUNCTION CHECKS FROM TOP LEFT TO BOTTOM RIGHT//")
for m in range(0,row):
    for n in range(0,col):
        num=int(input("ENTER NO:"))
        new.append(num)
    matrix.append(new)
    new=[]


a = np.array(matrix)
diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]
list1=[n.tolist() for n in diags]
print("//GIVEN MATRIX//")
for l in matrix:
    print(l)

len1=len(list1)
for i in range(0,len(list1)):
    temp=0
    for j in range(0,len(list1[i])):
            k=0
            if list1[i][j]==list1[i][k] :

                temp+=1
            k+=1
    if temp == len(list1[i]):
        numd+=1
if(numd==len1):
    print("IDENTICAL DIAGONALS")
else:
    print("NON IDENTICAL DIAGONALS")

