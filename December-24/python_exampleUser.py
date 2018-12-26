#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

def revstr(string,str,len):
    if(len!=0):
        str+=string[len]
        revstr(string,str,len-1)
    else:
        print(str)
def main():
    string=input("ENTER STRING")
    str=" "
    length1=len(string)
    revstr(string,str,length1-1)
if __name__ == '__main__':
    main()
