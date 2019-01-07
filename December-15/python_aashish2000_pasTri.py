n=int(input('rows= '))
def printPascal(n) : 
    for line in range(0, n) : 
        for i in range(0, line + 1) : 
            print(binomialCoeff(line, i), end = "") 
        print() 

def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
      
    return res 

printPascal(n+1)
lastrow=[]
for i in range(0,n+1):
	lastrow.append(binomialCoeff(n,i))

poly=''
x,y=n,0
c=0
while (x>=0):
	ans='('+str(lastrow[c])
	ans+='x^'
	ans+=str(x)
	ans+='y^'
	ans+=str(y)
	ans+=')'
	ans+='+'
	poly+=ans
	x-=1
	y+=1
	c+=1
print (poly[:len(poly)-1])