#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
def lucky(number,size):
    list1=[]
    temp=number
    number1=0
    for num in range(0,size):
        number1=temp % 10
        list1.append(number1)
        temp = temp/10

    sum1=0
    sum2=0
    for i in range(0,int((size/2)+1)):
        sum1+=list1[i]

    for i in range(int((size/2)+2),size):
        sum2+=list1[i]

    if sum1==sum2 :
        print("{} is a lucky number with sum {}".format(number,sum1))

    else:
        print("{} is a lucky number".format(number))

def main():
    n=int(input("enter the size of the number:"))
    number=int(input("enter the number:"))
    lucky(number,n)

if __name__ == '__main__':
    main()

