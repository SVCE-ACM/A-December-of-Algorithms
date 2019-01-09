m,n=map(int,input("Enter m, n: ").split())
mat=[]
for i in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
'''
ans=[i for i in mat[0]]
for i in range(1,n-1):
	ans.append(mat[i][m-1])
ans+=[i for i in mat[-1]]
for i in range(n-1, 0, -1):
	ans.append(mat[i][0])
for i in range
'''
def count(matrix, m, n):
	res=[k for k in matrix[0]]
	for l in range(1,n-1):
		res.append(matrix[l][m-1])
	newlst=matrix[n-1]
	newlst.reverse()
	res+=[a for a in newlst]
	for i in range(n-2, 0, -1):
		res.append(matrix[i][0])
	newlst=[]
	for i in range(1, n-1):
		newlst.append([i for i in matrix[i][1:m-1]])
	return res, newlst
#################################################
ans=[]
j=0
ans=[i for i in mat[0+j]]
#print (ans)
for i in range(1,n-1):
	ans.append(mat[i+j][m-1])
#print (ans)
newlst=mat[n-1-j]
newlst.reverse()
ans+=[i for i in newlst]
#print(ans)
for i in range(n-2-j, 0+j, -1):
	ans.append(mat[i][0])
#print (ans)
#################################################
newlst=[]
for i in range(1, n-1):
	newlst.append([i for i in mat[i][1:m-1]])
#print (newlst)
#################################################
if len(newlst)==1:
	for i in newlst[0]:
		ans.append(i)
	print (' --> '.join(map(str, ans)))
elif newlst==[]:
	print (' --> '.join(map(str, ans)))
else:
	while True:
		a,b=count(newlst, len(newlst[0]), len(newlst))
		#print(a,b)
		ans+=[e for e in a]
		if len(b)==0:
			break
		elif len(b)==1 and b[0]==[]:
			break
		elif len(b[0])==1:
			ans.append(b[0][0])
			break
		elif len(b[0][0])==0:
			break
		else:
			newlst=b[:]
			continue
	print(' --> '.join(map(str, ans)))