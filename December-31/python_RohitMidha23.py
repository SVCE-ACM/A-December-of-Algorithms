row=int(input("Enter the number of rows: "))
col=row
new=[]
one=[]
two=[]
matrix=[]
for m in range(0,row):
    for n in range(0,col):
        num=int(input("Enter Number:"))
        if(num in [0,1,2]):
         new.append(num)
         if num ==1 :
             one.append(m)
             one.append(n)
         if num == 2 :
             two.append(m)
             two.append(n)

        else:
            print("Error!")
            break
    matrix.append(new)
    new=[]
print("Matrix :")
for i in matrix:
    print(i)


if(one[0]==two[0]):
    if(one[1]>two[1]):
        print("Move {} steps left".format(one[1]-two[1]))
    else:
        print("Move {} steps right".format(two[1] - one[1]))

elif(one[1]==two[1]):
    if (one[0] > two[0]):
        print("Move {} steps up".format(one[0] - two[0]))
    else:
        print("Move {} steps down".format(two[0] - one[0]))
else:
    if two[0]>one[0]:
        print("Move {} steps down".format(two[0]-one[0]))
        if(two[1] > one[1]):
            print("Move {} steps right".format(two[1]-one[1]))
        else:
            print("Move {} steps left".format(one[1] - two[1]))
    else:
        print("Move {} steps down".format(one[0] - two[0]))
        if (two[1] > one[1]):
            print("Move {} steps right".format(two[1] - one[1]))
        else:
            print("Move {} steps left".format(one[1] - two[1]))
