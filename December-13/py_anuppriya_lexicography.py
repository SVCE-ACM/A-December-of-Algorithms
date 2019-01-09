
def fact(n) : 
    f = 1
    while n >= 1 : 
        f = f * n 
        n = n - 1
    return f 
      
def findsmall(str, low, high) : 
      
    countRight = 0
    i = low + 1
    while i <= high : 
        if str[i] < str[low] : 
            countRight = countRight + 1
        i = i + 1
    return countRight 
    
def findRank (str) : 
    ln = len(str) 
    mul = fact(ln) 
    rank = 1
    i = 0 
   
    while i < ln : 
        mul = mul / (ln - i) 
        countRight = findsmall(str, i, ln-1) 
        rank = rank + countRight * mul 
        i = i + 1
    return rank 
      
str = input("Enter the String :")
print (findRank(str)) 
  
