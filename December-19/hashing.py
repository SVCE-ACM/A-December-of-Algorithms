#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

def hashstr(string1):
    list1=[]
    list2=[]
    sum=0
    for ltr in string1:
        list1.append(ltr)
    for ltrr in list1:
        list2.append(ord(ltrr))
    for num in list2:
        sum+=num
    print(sum/len(string1))

def main():
    string=input("ENTER STRING TO HASH:")
    hashstr(string)
if __name__ == '__main__':
    main()


