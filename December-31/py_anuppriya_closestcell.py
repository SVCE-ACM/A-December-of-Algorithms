coord=[]
l=[]
#strArr="000","100","200"
def ClosestCell2(strArr):
    for i in range(len(strArr)):
        for j in range(len(strArr[0])):
               if strArr[i][j]=="1":
                   x,y=i,j
    for i in range(len(strArr)):
        for j in range(len(strArr[0])):
            if strArr[i][j]=="2":
                   coord.append((i,j))             
    m=100
    for a,b in list(coord):
           n=abs(x-a)+abs(y-b)
           l.append(min(m,n))
    #print(coord)                       
strArr=input("Enter array elements(seperated by ,): ").split(",")
ClosestCell2(strArr)
print("Given matrix: ")
for i in range(len(strArr)):
    for j in range(len(strArr[0])):
        print(strArr[i][j],end=" ")
    print("",sep="\n")    
if len(coord)==0:
         print("Output: 0")  
print("Output: ",min(l))
