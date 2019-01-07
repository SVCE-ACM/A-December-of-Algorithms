import math
clno=int(input("Number of classrooms:"))
clsize=int(input("Size of classrooms (1-50):"))
deptno=int(input("Enter the number of departments (2-10): "))
deptlist=[]
for x in range(deptno):
	print(("Department "+str(x+1)+" Code: "))
	deptlist.append(input())
studno=[]
for x in range(deptno):
    studno.append(int(input("Students in department "+str(x+1)+" (1-100): ")))

res=[0]*clno

row=math.ceil(clsize**(0.5))
col=row

count=[1]*deptno
for x in range(clno):
	elecnt=0
	f=0
	print("\nROOM "+str(x+1))
	for i in range(row):
		for j in range(col):
			elecnt+=1
			idno=(i+j)%deptno
			if(studno[idno]>=count[idno]):
				print(deptlist[idno]+str(count[idno]),end=' ')
				count[idno]+=1
			else:
				print('____',end=' ')
			if(elecnt==clsize):
				f=1
				break
		print("")
		if(f==1):
			break

