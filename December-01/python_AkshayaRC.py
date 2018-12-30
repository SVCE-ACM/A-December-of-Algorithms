l=[]
num=int(input("enter size of list"))
print("enter list elements")
for i in range(num):
   l.append(int(input()))   
l.sort()
#print(l)
n=int(input("Choose a number"))
low=0
high=num-1
##print(low,high)
while(low<=high):
   mid=int((low+high)/2)
   print(l[mid],"(half of ",l[low],"to ",l[high],") -->",end=" ")
   if(l[mid]==n):
      print("spot on!")
      break
   else:   
     if(l[mid]>n):
        print("you're too high")
        high=mid-1
     if(l[mid]<n):
        print("you're too low")
        low=mid+1
   if low>high:
      print("not found!")
     
