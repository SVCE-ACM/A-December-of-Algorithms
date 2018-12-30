#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
def roundnum(num,dgt):
    return (round(num,dgt))

def main():
    num=float(input("Enter the decimal number:"))
    round=int(input("No. of digits to be rounded off:"))
    result=roundnum(num,round)

    print("Round off value is:",result)
if __name__ == '__main__':
    main()
