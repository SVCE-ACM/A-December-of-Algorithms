#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

def cup_n_str(num):
    print("NO. OF STRINGS REQUIRED IS:",(num*(num-1)/2))
def main():
    num=int(input("ENTER THE NO. OF FRIENDS:"))
    cup_n_str(num)
if __name__ == '__main__':
    main()
