#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
import itertools
def lex(li,s):
    li=list(itertools.permutations(li))
    li=[''.join(combos) for combos in li]
    li.sort()
    print(li,"\n")
    for i in range(len(li)):
        if li[i]==s :
            print("position:",str(i+1))
def main():
    s=input("ENTER STRING:")
    lex(list(s),s)
if __name__ == '__main__':
    main()
