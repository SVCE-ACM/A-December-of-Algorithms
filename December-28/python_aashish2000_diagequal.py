import numpy
mat=[]
print("Input matrix = ")
while True:
	lst=str(input(""))
	if lst[0]=='[':
		mat.append(lst[1:].split())
	elif lst[-1]==']':
		mat.append(lst[:-1].split())
		break
	else:
		mat.append(lst.split())
	
a=numpy.array(mat)
diags=[a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1)]
res="Identical diagonals"
for i in diags:
	if list(i)==list(i)[::-1]:
		pass
	else:
		res="Diagonals are non-identical"
		break
print (res)
