#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
def fib(term):
    num1=0
    num2=1
    while term>0 :
        num3=num1+num2
        print(num1)
        num1=num2
        num2=num3
        term-=1

def main():
    terms=int(input("enter the number of terms"))
    fib(terms)
if __name__ == '__main__':
    main()

