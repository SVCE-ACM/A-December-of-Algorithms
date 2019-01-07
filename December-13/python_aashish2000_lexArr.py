def binarySearch (arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l)//2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x)  
        else: 
            return binarySearch(arr, mid + 1, r, x) 
    else: 
        return -1

from itertools import permutations
s=str(input())
all_perm=[]
for string in permutations(s):
    if((''.join(string)) not in all_perm):
        all_perm.append(''.join(string))
all_perm.sort()
index=binarySearch(all_perm, 0, len(all_perm)-1, s)
print (index+1)
