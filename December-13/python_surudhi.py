from itertools import permutations
S=input('Enter the word ')
print('Possible Combinations: ')
print('\n'.join(sorted(''.join(p) for p in permutations(S,len(S)))))
t=sorted(''.join(p) for p in permutations(S,len(S)))
k=t.index(S)
print('Position of',S,'is',k+1)
