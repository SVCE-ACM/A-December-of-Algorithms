#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
def printPascal(n):
    list1=[]
    for line in range(0, n):
        for i in range(0, line + 1):
            list1.append(binomialCoeff(line, i))
    l=len(list1)
    l-=n

    while(l<len(list1)):
        j = 0
        for i in range(n-1,-1,-1):
         print(list1[l],"a^",i,"b^",j)
         l+=1
         j+=1





def binomialCoeff(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res

def main():

   n =int(input("ENTER THE NO:"))
   printPascal(n+1)

if __name__ == '__main__':
    main()
