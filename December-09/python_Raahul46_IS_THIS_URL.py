#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

import validators
def isurl(link):
   value=validators.url(link)

   if(value==True):
       print("It is a URL")
   else:
       print("It is not a URL")

def main():
    string=str(input("ENTER THE URL TO CHECK:"))
    isurl(string)
if __name__ == '__main__':
    main()

