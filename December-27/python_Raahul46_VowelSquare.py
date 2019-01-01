#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

def vowels(list1):
    l1=len(list1)
    flag=0
    for i in range(l1 - 1):
        l2=len(list1[i])
        for l in range(l2 - 1):
            if list1[i][l] in 'aeiou' and list1[i][l+1] in 'aeiou' and list1[i+1][l] in 'aeiou' and list1[i+1][l+1] in 'aeiou':
                print(i,'==',l)
                flag=1
    if(flag==0):
        print("Unavailable")
str=input("STRING:")
vowels(str.split())
