mat=list(map(str,input("strArr: ").split(',')))

vovel="aeiouAEIOU"
matmap=[]
for x in range(len(mat)-1):
	for y in range(len(mat[0])-1):
		if(mat[x][y] in vovel and mat[x+1][y] in vovel and mat[x][y+1] in vovel and mat[x+1][y+1] in vovel):
			matmap.append([x,y])
			break

if(matmap!=[]):
	print(str(matmap[0][0])+"-"+str(matmap[0][1]))
else:
	print("Unavailable")




