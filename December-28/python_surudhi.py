import itertools
def compare(a, b):
    return 0 if a == b else 1
c=int(input('Enter the number of columns: '))
test=[]
flag=0
for i in range(c):
    a = [int(x) for x in input('Enter the row elements: ').split()]
    test.append(a)
print('Input Matrix:',test)
max_col = len(test)
max_row = len(test[0])
min_bdiag = -max_col + 1
fdiag = [[] for i in range(max_col + max_row - 1)]
bdiag = [[] for i in range(len(fdiag))]
for y in range(max_col):
    for x in range(max_row):
        bdiag[-min_bdiag+x-y].append(test[y][x])
x=[]
for i in bdiag:
    flag=1
    for j in i:
        minimum = i[0]
        if j!=minimum:
            flag=0
            break
    x.append(flag)
print('Diagonal elements:',bdiag)
b=True
for item in x:
    if not item:
        b=False
        break;
if b:
    print( "Identical Diagonals")
else:
    print("Diagonals are not identical")
        
