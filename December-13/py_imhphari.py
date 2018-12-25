def fact(n): 
    f=1
    while n>=1: 
        f=f*n 
        n=n-1
    return f 
      
def sm(st,low,high) : 
      
    countRight=0
    i=low+1
    while i<=high : 
        if st[i]<st[low] : 
            countRight=countRight+1
        i=i+1
   
    return countRight 

def rank(str) : 
    ln = len(str) 
    mul = fact(ln) 
    rank = 1
    i = 0 
   
    while i<ln : 
          
        mul=mul/(ln-i) 
        countRight=sm(str,i,ln-1) 
   
        rank=rank+countRight*mul 
        i=i+1
          
    return rank 

str = input ("Enter the string:")
print (rank(str)) 
