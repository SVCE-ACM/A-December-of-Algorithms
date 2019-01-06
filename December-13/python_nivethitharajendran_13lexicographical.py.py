from itertools import permutations 
a=[] 
def allPermutations(str): 
     permList = permutations(str) 
     for perm in list(permList): 
         a.append(''.join(perm)) 

x=input("Enter the word")
allPermutations(x)
z=1   
a.sort()
for i in a:
  if i==x:
    print(z)
  else:
    z=z+1  
