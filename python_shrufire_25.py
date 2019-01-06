from numpy import*

a=[]
for i in range(100):
    a.append('*')  
b=array([a])
c=reshape((a),(10,10))
a=input('Enter the location of Santa: ')
b=input('Enter the location of Kid: ')
a1=[]
b1=[]
for y in a.split(','):
    a1.append(int(y))
for y in b.split(','):
    b1.append(int(y))
c[a1[0]][a1[1]]='S'
c[b1[0]][b1[1]]='K'


if a1[0]<b1[0]:
    i=a1[0]+1
    while i!=b1[0]:
        c[i][a1[1]]=" "
        i+=1
    c[i][a1[1]]=" "    
    j=a1[1]    
    while j!=b1[1]:
        c[i][j]=" "
        j+=1
else:
    i=b1[0]+1
    while i!=a1[0]:
        c[i][b1[1]]=" "
        i+=1
    c[i][b1[1]]=" "    
    j=b1[1]    
    while j!=a1[1]:
        c[i][j]=" "
        j+=1
print(c)        

   
    

    
  
