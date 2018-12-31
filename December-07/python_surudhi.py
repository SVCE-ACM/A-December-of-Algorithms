def round(n):
    i=n-int(n)
    if i:
        if i>0.5:
            n=float(int(n)+1)
            return n
        else:
            n=float(int(n)-1)
            return n
    else:
        return n
a=float(input('Enter the first number: '))
b=float(input('Enter the second number: '))
tol=float(input('Enter the tolerance level: '))
c=round(a)
d=round(b)
if (c==d) and abs(a-b)<tol:
    print(True)
else:
    print(False)
