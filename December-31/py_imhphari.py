c=[]
l=[]
def clos(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
               if a[i][j]=="1":
                   x,y=i,j
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]=="2":
                   c.append((i,j))             
    m=100
    for a,b in list(c):
           n=abs(x-a)+abs(y-b)
           l.append(min(m,n))
                         
a=input("Enter array elements(seperated by ,): ").split(",")
clos(a)
print("Given matrix: ")
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j],end=" ")
    print(" \n")    
if len(c)==0:
         print("Output: 0")  
print("Output: ",min(l))
