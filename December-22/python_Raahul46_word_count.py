#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

import sys
import operator

def storewords(filename,string):
    with open('filename.txt', 'w') as f:
     dict={}
     str1=" "
     for word in string.split():
                if word in dict:
                    dict[word]=dict[word]+1
                else:
                    dict[word]=1
     dict = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
     str1=str(dict)
     f.write(str1)
     f.close()
    return dict

def print_words(filename,string):
    dict=storewords(filename,string)
    for k in range(0,len(dict)):
        print (dict[k][0], dict[k][1])
    with open('filename.txt', 'r') as f:
        print("IN FILE>>>>")
        for word in f:
            print(word)


def main():
 string=input("ENTER THE STRING:")
 filename=input("ENTER THE FILENAME:")
 print_words(filename,string)
if __name__ == '__main__':
  main()
