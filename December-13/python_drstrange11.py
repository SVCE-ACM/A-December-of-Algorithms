# Dec 13
from itertools import permutations
s = input("Enter string: ")
fin = list(set(permutations(list(s))))
fin.sort()
print('The order')
for ind, letters in enumerate(fin):
    word = ''.join(x for x in letters)
    if word == s:
        print(f"{word} --> Match found at position {ind+1}")
    else:
        print(word)

# Sample I/O
# Enter string: dac
# The order
# acd
# adc
# cad
# cda
# dac --> Match found at position 5
# dca
