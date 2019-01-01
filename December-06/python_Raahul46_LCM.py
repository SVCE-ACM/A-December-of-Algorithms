#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
def lcm(num1,num2):
    list1=[]
    list2=[]
    flag=0
    if (num1>num2) :
        for i in range(1, num1):
            list1.append(num1 * i)
            list2.append(num2 * i)
        for numb1 in list1:
            for numb2 in list2:
                if numb1 == numb2:
                    flag=1
                    return numb1

    elif(num1<num2):
        for i in range(1, num2):
            list1.append(num1 * i)
            list2.append(num2 * i)
        for numb1 in list1:
            for numb2 in list2:
                if numb1 == numb2:
                    flag=1
                    return numb1


    else:
        return num1

    if (flag == 0):
        return num1 * num2


def main():
    n=int(input("Enter the no. of numbers:"))
    list1=[]
    for i in range(0,n):
        number=int(input("Enter the number:"))
        list1.append(number)

    num1=list1[0]
    num2=list1[1]
    lc=lcm(num1,num2)
    for i in range(2,len(list1)):

        lc=lcm(lc,list1[i])
    print("The least common factor is:",lc)
if __name__ == '__main__':
    main()


