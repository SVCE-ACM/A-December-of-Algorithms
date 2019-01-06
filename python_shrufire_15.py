def printPascal(n) :
    for line in range(0, n) :
        x=''
        for i in range(0, line + 1) :
            y=str(binomialCoeff(line, i))+'   '
            x=x+y
        print(x,'-->','Row',line)
        print() 
def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
    return res 
n=int(input('Enter the number of rows: '))
printPascal(n+1)
str2=''
for i in range(n+1):
    str1=str(binomialCoeff(n,i))+'a^'+str(n-i)+'b^'+str(i)
    if i!=n:
        str2=str2+str1+'+'
    else:
        str2=str2+str1
print('Polynomial:',str2)
