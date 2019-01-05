from numpy import *
def printsquare(m):
    if m%2!=0:
        k =[[0 for i in range(m)] for j in range(m)]
        r=0;
        c=int(m/2);
    for i in range(1,m*m+1):
        k[r][c]= i;
        br = r+1;
        bc = c+1;
        r=(r+m-1)%m;
        c=(c+1)%m;
        if k[r][c]!=0:
            r=br;
            c=bc-1;
    sq=[]
    for row in k:
        sq.append(row)
    s=array([sq])
    s1=reshape(s,(m,m))
    print(s1)
    print('\n')
    s2=trans(s1,m)
    s=array([s2])
    s1=reshape(s,(m,m))
    print(s1)
    print('\n')
    list.reverse(sq)
    s=array([sq])
    s1=reshape(s,(m,m))
    print(s1)
    print('\n')
    s2=trans(s1,m)
    s=array([s2])
    s1=reshape(s,(m,m))
    print(s1)
    print('\n')
    sq=[]
    for row in k:
        list.reverse(row)
        sq.append(row)
    s=array([sq])
    s1=reshape(s,(m,m))
    print(s1)
    print('\n')
    s2=trans(s1,m)
    s=array([s2])
    s1=reshape(s,(m,m))
    print(s1)
    print('\n')
    list.reverse(sq)
    s=array([sq])
    s1=reshape(s,(m,m))
    print(s1)
    print('\n')
    s2=trans(s1,m)
    s=array([s2])
    s1=reshape(s,(m,m))
    print(s1)
    print('\n')
def trans(X,n):
    result=[]
    for i in range(n):
        s=[]
        for j in range(n):
            s.append(0)
        result.append(s)
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
    return result
n=int(input('Order: '))
sum=n*(n*n+1)/2
print('Magic Sum: ',sum)
printsquare(n)
