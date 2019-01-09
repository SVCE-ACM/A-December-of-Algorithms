def ClosestCell2(arr):
    r = len(arr)
    c = len(arr[0])
    s = 99999
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                break
        if arr[i][j] ==1:
            break
    for k in range(r):
        for l in range(c):
            if arr[k][l]==2:
                x = abs(i-k)+abs(j-l)
                if x<s:
                    s = x
                    print('Output:',s)
                    return
    if s>0:
        print(s)
    else:
        print(0)
m = int(input('Enter number of rows :'))
n = int(input('Enter number of columns :'))
mat= [[0 for i in range(n)] for j in range(m)]
print('Enter elements of matrix one by one')
for i in range(m):
    for j in range(n):
        mat[i][j] = int(input())
ClosestCell2(mat)
