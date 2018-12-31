def path(x, y, a, b):  
    x, y, a, b = abs(x), abs(y), abs(a), abs(b)  
    fin=[]
    if b==y and a==x:
        print('Both coordinates are same')
    elif b==y:
        print('(',x,',',y,') --> (',a,',',b,')')
        for j in range(10):
            p=[]
            if j==b:
                for i in range(x):
                    p.append('*')
                p.append('S')
                for i in range(a-x-1):
                    p.append(' ')
                p.append('K')
                for i in range(9-a):
                    p.append('*')
            else:
                for i in range(10):
                    p.append('*')
            fin.append(p)
    elif x==a:
        print('(',x,',',y,') --> (',a,',',b,')')
        for j in range(10):
            p=[]
            if j>y and j<b:
                for i in range(x):
                    p.append('*')
                p.append(' ')
                for i in range(x+1,10):
                    p.append('*')
            elif j==y:
                for i in range(x):
                    p.append('*')
                p.append('S')
                for i in range(x+1,10):
                    p.append('*')
            elif j==b:
                for i in range(x):
                    p.append('*')
                p.append('K')
                for i in range(x+1,10):
                    p.append('*')
            else:
                for i in range(10):
                    p.append('*')
            fin.append(p)
    else:
            print('(',x,',',y,') --> (',x,',',b,') --> (',a,',',b,')')            
    for i in range(10):
        print(fin[i])
x=int(input('Enter the first x-coordinate: '))
y=int(input('Enter the first y-coordinate: '))
a=int(input('Enter the second x-coordinate: '))
b=int(input('Enter the second y-coordinate: '))
path(x,y,a,b)
