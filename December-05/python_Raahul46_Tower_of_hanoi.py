#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
def Movetower(height,fromPole, toPole, withPole):
    if height >= 1:
        Movetower(height-1,fromPole,withPole,toPole)
        Movedisk(fromPole,toPole)
        Movetower(height-1,withPole,toPole,fromPole)

def Movedisk(fp,tp):
    print("moving disk from",fp,"to",tp)

def main():
    number=int(input("Enter no. of disks:"))
    Movetower(number,"A","B","C")

if __name__ == '__main__':
    main()
