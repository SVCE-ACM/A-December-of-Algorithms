def binarySearch(l,r,x):
    mid=l+(r-l)//2
    print("Guess",mid,"(half of",l,"and",r,")",end=" ")
    if(mid>x):
        print("->you're too high")
        binarySearch(l,mid-1,x)

    if(mid<x):
        print("->you're too low")
        binarySearch(mid+1,r,x)
    if(mid==x):
        print("->spot on!")

no=int(input("Enter Secret Number:"))
l=0
r=100
while True:
    if(r<no):
        r+=100
        l+=100
    else:
        break

print("Performing Binary Search")

binarySearch(l,r,no)
