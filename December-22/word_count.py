#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

import string
def word_count(string1):
    list1=string1.split()
    list4=[]
    list3=[]
    str=string.digits
    for ltr in str:
        list4.append(ltr)

    for i in list1:
        temp=0
        for j in list1:
            if i==j:
                temp+=1

        list3.append(i)
        list3.append(temp)

    for i in range(0,len(list3),2):
        print("word:",list3[i],"is repeated:",list3[i+1])


def main():
    word_count("Martha! Why did you say that name? Please! Stop! Why did you say that name?")
if __name__ == '__main__':
    main()
