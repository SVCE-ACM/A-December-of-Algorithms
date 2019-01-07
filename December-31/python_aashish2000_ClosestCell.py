mat=list(map(str,input("2D Matrix input: ").split(',')))

lx=0
ly=0
f=0
loc2=[]
for x in range(len(mat)):
	for y in range(len(mat[0])):
		if(mat[x][y]=='1'):
			f=1
			lx=int(x)
			ly=int(y)
		if(mat[x][y]=='2'):
			loc2.append([int(x),int(y)])
if(loc2!=[]):
	dist=[]
	for i in range(len(loc2)):
		ax=abs(loc2[i][0]-lx)
		bx=abs(len(mat[0])-ax)
		ay=abs(loc2[i][1]-ly)
		by=abs(len(mat[1])-ay)
		dist.append(min(ax,bx)+min(ay,by))

	print("Output: ",min(dist))
else:
	print("Output: ",0)

