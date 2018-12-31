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
    print(sq)
    list.reverse(sq)
    print(sq)
    sq=[]
    for row in k:
        list.reverse(row)
        sq.append(row)
    print(sq)
    list.reverse(sq)
    print(sq)
n=int(input('Order: '))
sum=n*(n*n+1)/2
print('Magic Sum: ',sum)
printsquare(n)
