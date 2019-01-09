matrix=[["*" for i in range(0,10)] for j in range(0,10)] 
print("\nSanta's location(row-column) (seperated by new line): ")
sr=int(input())
sc=int(input())
print("Child's location(row-column) (seperated by new line): ")
cr=int(input())
cc=int(input())
#print(sr,sc,cr,cc)
j=sc
for i in range(sr,cr+1):
        if matrix[i][j]=="*":
            matrix[i][j]=" "
matrix[sr][sc]="S"            
i=cr
for j in range(sc+1,cc+1):
    if matrix[i][j]=="*":
        matrix[i][j]=" "
if sc>cc:
    for j in range(sc-1,cc,-1):
       if matrix[i][j]=="*":
        matrix[i][j]=" "
matrix[cr][cc]="K"

if cr<sr:
    j=sc
    for i in range(sr,cr-1,-1):
       if matrix[i][j]=="*":
        matrix[i][j]=" " 
print("A path between santa at (",sr,",",sc,") and child at (",cr,",",cc,"): ")
print("*",end=" ")
for i in range(10):
    print(i,end=" ")
print("",sep="\n")
for i in range(0,10):
    print(i,end=" ")
    for j in range(0,10):
      print(matrix[i][j],end=" ")
    print("",sep="\n")              
