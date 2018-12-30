#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

def no_of_diagonals(num):
    print("NO. OF DIAGONALS IS:",(num*(num-3)/2))
def main():
    num=int(input("ENTER THE NO. OF VERTEX:"))
    no_of_diagonals(num)
if __name__ == '__main__':
    main()
