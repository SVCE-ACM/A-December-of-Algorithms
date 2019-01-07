import math
import numpy as np

def DoublyEven(n): 
      
    arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)] 
  
    for i in range(0,n//4): 
        for j in range(0,n//4): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
      
    for i in range(0,n//4): 
        for j in range(3 * (n//4),n): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
  
    for i in range(3 * (n//4),n): 
        for j in range(0,n//4): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
      
    for i in range(3 * (n//4),n): 
        for j in range(3 * (n//4),n): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
              
    for i in range(n//4,3 * (n//4)): 
        for j in range(n//4,3 * (n//4)): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
    return(arr) 
    '''for i in range(n): 
        for j in range(n): 
            print ('%2d ' %(arr[i][j]),end='') 
        print("")'''

def generateSquare(n): 
  
    # 2-D array with all  
    # slots set to 0 
    magicSquare = [[0 for x in range(n)] 
                      for y in range(n)] 
  
    # initialize position of 1 
    i = n / 2
    j = n - 1
      
    # Fill the magic square 
    # by placing values 
    num = 1
    while num <= (n * n): 
        if i == -1 and j == n: # 3rd condition 
            j = n - 2
            i = 0
        else: 
              
            # next number goes out of 
            # right side of square  
            if j == n: 
                j = 0
                  
            # next number goes  
            # out of upper side 
            if i < 0: 
                i = n - 1
                  
        if magicSquare[int(i)][int(j)]: # 2nd condition 
            j = j - 2
            i = i + 1
            continue
        else: 
            magicSquare[int(i)][int(j)] = num 
            num = num + 1
                  
        j = j + 1
        i = i - 1 # 1st condition
    return(magicSquare) 
  
    # Printing magic square 
      
    '''for i in range(0, n): 
        for j in range(0, n): 
            print('%2d ' % (magicSquare[i][j]),  
                                     end = '') 
              
            # To display output  
            # in matrix form 
            if j == n - 1:  
                print()''' 
          
def singleEven(s):
    LOG_10 = 2.302585092994
     
     
    # build odd magic square
    def build_oms(s):
        if s % 2 == 0:
            s += 1
        q = [[0 for j in range(s)] for i in range(s)]
        p = 1
        i = s // 2
        j = 0
        while p <= (s * s):
            q[i][j] = p
            ti = i + 1
            if ti >= s: ti = 0
            tj = j - 1
            if tj < 0: tj = s - 1
            if q[ti][tj] != 0:
                ti = i
                tj = j + 1
            i = ti
            j = tj
            p = p + 1
     
        return q, s
     
     
    def build_sems(s):
        if s % 2 == 1:
            s += 1
        while s % 4 == 0:
            s += 2
     
        q = [[0 for j in range(s)] for i in range(s)]
        z = s // 2
        b = z * z
        c = 2 * b
        d = 3 * b
        o = build_oms(z)
     
        for j in range(0, z):
            for i in range(0, z):
                a = o[0][i][j]
                q[i][j] = a
                q[i + z][j + z] = a + b
                q[i + z][j] = a + c
                q[i][j + z] = a + d
     
        lc = z // 2
        rc = lc
        for j in range(0, z):
            for i in range(0, s):
                if i < lc or i > s - rc or (i == lc and j == lc):
                    if not (i == 0 and j == lc):
                        t = q[i][j]
                        q[i][j] = q[i][j + z]
                        q[i][j + z] = t
     
        return q, s
     
     
    def format_sqr(s, l):
        for i in range(0, l - len(s)):
            s = "0" + s
        return s + " "
     
     
    def display(q):
        return(q[0])
        '''s = q[1]
        k = 1 + math.floor(math.log(s * s) / LOG_10)
        for j in range(0, s):
            for i in range(0, s):
                print(format_sqr("{0}".format(q[0][i][j]), k),end='')
            print()'''
    mat=display(build_sems(s))
    return(mat)
 
 

n=int(input("Enter Order: "))
magsum=int(input("Enter Magic Sum: "))
if(n%2==0 and n%4!=0):
    result=singleEven(n)
elif(n%2==0):
    result=DoublyEven(n)
else:
    result=generateSquare(n)

print("Magic Matrices (Output): ")
m = np.array(result, int)
new=m
for x in range(8):
    for i in range(0, n): 
        for j in range(0, n): 
            print('%2d ' % (new[i][j]),  end = '') 
            if j == n - 1:  
                print() 
    print("\n")

    if(x%2==0):
        new=new.transpose()
    else:
        new=np.rot90(m,(x+1)//2)



