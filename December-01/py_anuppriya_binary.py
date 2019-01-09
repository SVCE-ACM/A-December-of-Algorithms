def bs(a, l, r, x): 
    if r >= l: 
        mid =int((l+r)/2)
        print("Guess: ",a[mid],"Between",a[l],"and",a[r])
        if a[mid] == x: 
            return mid

        elif a[mid] > x: 
            return bs(a, l, mid-1, x) 

        else: 
            return bs(a, mid + 1, r, x) 
    else: 
        return -1
  
s=int(input("Enter size:"))
a=[0]*s
print("Enter List: ")
for i in range(s):
  a[i]=int(input())

print(a)
x=int(input("\nEnter the Key:"))
result = bs(a, 0, len(a)-1, x) 
if result != -1: 
    print ("Element is present at index:",result )
else: 
    print ("Element is not present in array")
