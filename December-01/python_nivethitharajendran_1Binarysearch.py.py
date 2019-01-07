# Returns index of x in arr if present, else -1
def binarySearch ( l, r, x):
    
    
# Check base case
    if r >= l:
        mid =int( l + (r-l)/2)
# If element is present at the middle itself
        if mid == x:
            return mid
            print("Spot on!")
# If element is smaller than mid, then it
# can only be present in left subarray
        elif mid > x:
            print (mid,"You are too high")
            return binarySearch( l, mid-1, x)
# Else the element can only be present
# in right subarray
        else:
           print(mid,"You are too low")
           return binarySearch( mid + 1, r, x)
    else:
        
        # Element is not present in the array 
        return -1


# Test array
x=38
# Function call
result=binarySearch( 1, 99, x)
if result!=-1:
    print("Your guess is right!")



