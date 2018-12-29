#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

row=int(input("ENTER THE NO. OF ROWS:"))
col=row
new=[]
one=[]
two=[]
matrix=[]
for m in range(0,row):
    for n in range(0,col):
        num=int(input("ENTER NO:"))
        if(num in [0,1,2]):
         new.append(num)
         if num ==1 :
             one.append(m)
             one.append(n)
         if num == 2 :
             two.append(m)
             two.append(n)

        else:
            print("error")
            break
    matrix.append(new)
    new=[]
print("//GIVEN MATRIX//")
for m in matrix:
    print(m)


if(one[0]==two[0]):
    if(one[1]>two[1]):
        print("MOVE {} STEPS LEFT".format(one[1]-two[1]))
    else:
        print("MOVE {} STEPS RIGHT".format(two[1] - one[1]))

elif(one[1]==two[1]):
    if (one[0] > two[0]):
        print("MOVE {} STEPS UP".format(one[0] - two[0]))
    else:
        print("MOVE {} STEPS DOWN".format(two[0] - one[0]))
else:
    if two[0]>one[0]:
        print("MOVE {} steps down".format(two[0]-one[0]))
        if(two[1] > one[1]):
            print("MOVE {} steps right".format(two[1]-one[1]))
        else:
            print("MOVE {} steps left".format(one[1] - two[1]))
    else:
        print("MOVE {} steps down".format(one[0] - two[0]))
        if (two[1] > one[1]):
            print("MOVE {} steps right".format(two[1] - one[1]))
        else:
            print("MOVE {} steps left".format(one[1] - two[1]))
