#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
def binarySearch(arr, l, r, x):

    if r >= l:

        mid = int(l + (r - l) / 2)


        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)

    else:

        return -1
arr=[]
number=0
num=int(input("ENTER NO. OF NUMBERS"))
for i in range(0,num):
    number=int(input("ENTER NUMBER:"))
    arr.append(number)
x = int(input("ENTER THE NUMBER TO SEARCH:"))
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
