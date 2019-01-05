x1=input('Enter the three sides of the first triangle: ')
x2=input('Enter the three angles of the first triangle: ')
x3=input('Enter the three sides of the second triangle: ')
x4=input('Enter the three angle of the second triangle: ')
x1.split()
p1=[]
for y in x1.split():
    p1.append(int(y))
x2.split()
q1=[]
for y in x2.split():
    q1.append(int(y))
x3.split()
p2=[]
for y in x3.split():
    p2.append(int(y))
x4.split()
q2=[]
for y in x4.split():
    q2.append(int(y))
p1.sort()
p2.sort()
q1.sort()
q2.sort()
if p1[0]/p2[0]==p1[1]/p2[1] and p1[1]/p2[1]==p1[2]/p2[2] and  p1[2]/p2[2]==p1[0]/p2[0]:
    flag1=1
else:
    flag1=0
if q1[0]==q2[0] and q1[1]==q2[1] and q1[2]==q2[2]:
    flag2=1
else:
    flag2=0
if (p1[0]/p2[0]==p1[1]/p2[1] and q1[2]==q2[2]) or (p1[1]/p2[1]==p1[2]/p2[2] and q1[0]==q2[0]) or (p1[0]/p2[0]==p1[2]/p2[2] and q1[1]==q2[1]):
    flag3=1
else:
    flag3=0
if flag1 or flag2 or flag3:
    print('Triangles are similar by ')
    if flag1: print('SSS ')
    if flag2: print('AAA ')
    if flag3: print('SAS ')
else:
    print('Triangles are not similar')
    
