def binary_search(arr,l,r,ele):
    while l<=r:
        mid=l+(r-1)//2
        if arr[mid]==ele:
            print("Guess",mid,"(half of",l,"to",r,")->you found")
            return mid
        elif arr[mid]<ele:
            print("Guess",mid,"(half of",l,"to",r,")->you'r to high")
            l=mid+1
        else:
            print("Guess",mid,"(half of",l,"to",r,")->you'r to low")
          
            r=mid-1
    return -1
arr=[10,20,30,40,50]
ele=30
pos=binary_search(arr,0,len(arr)-1,ele)

if pos!=-1:
    print("\nElement present in",pos,"position")
else:
    print("Element not found")
