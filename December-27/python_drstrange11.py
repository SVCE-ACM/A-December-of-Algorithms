# Dec 27
import numpy as np


def VowSq(strArr):
    l = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for s in strArr:
        l.append(list(s))
    l = np.array(l)
    check = len(l[0])*len(l)
    print(l)
    if check % 4 == 0:
        if check < 8:
            print("Unavailable")
        else:
            for i in range(len(l)-1):
                for j in range(len(l[0])-1):
                    if l[i, j] in vowels and l[i+1, j] in vowels and l[i, j+1] in vowels and l[i+1, j+1] in vowels:
                        print(f"{i}-{j}")
                        break
    else:
        print("Unavailable")


# Make sure all the elements in each row are same
arr = input("Enter the strings: ").split()
VowSq(arr)

# SAMPLE I/O
# Enter the strings: abcd eikr oufj
# [['a' 'b' 'c' 'd']
#  ['e' 'i' 'k' 'r']
#  ['o' 'u' 'f' 'j']]
# 1-0
