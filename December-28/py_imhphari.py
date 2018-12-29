import numpy as np
import itertools

matrix = np.array(
         [[7 ,4,6,8], 
        [1,7,4,6],
         [9,1,7,4]])

diags = [matrix[::-1,:].diagonal(i) for i in range(3,4)]
diags.extend(matrix.diagonal(i) for i in range(3,-4,-1))

for n in diags:
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if(n[i]==n[j]):
                print("Identical")
    

#print ([n.tolist() for n in diags])
