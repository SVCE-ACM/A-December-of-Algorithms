def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = int((first + last)//2)
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found
a=[]
n=int(input("enter the no of elements"))
for i in range (0,n):
    a.append(int(input()))
a.sort()
m=int(input("enter the element to search"))
print(binarySearch(a,m))
