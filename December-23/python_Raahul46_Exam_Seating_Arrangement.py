#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
n = int(input('Enter number of classrooms'))
nb = int(input('enter number of benches'))
nd = int(input('enter number of depts'))
dn = (input('enter names of depts separated by ,'))
dn = dn.split(',')
dict = {}
ns = (input('Enter number of students in each dept'))
ns = ns.split(',')
ns = [ int(no) for no in ns]
nrc = int(nb**(1/2))

it = 0
rn = [ 0 for x in range(nd)]
for room in range(n):
	a = [['__' for x in range(nrc)] for y in range(nrc)]
	row = 0
	coloumn = 0
	print('Room',room+1)
	while(row<nrc and coloumn<nrc):
		if  a[row-1][coloumn][0:2]==dn[it]:
			it = (it+1)%nd
			if nd==1:
				coloumn += 1
				if coloumn==nrc:
					coloumn = 0
					row += 1
				else:
					coloumn += 1

		if a[row][coloumn] =='__':
			rn[it] += 1
			a[row][coloumn] = dn[it]+str(rn[it])
			coloumn += 1
			if coloumn == nrc:
				row += 1
				coloumn = 0
			ns[it] -= 1
			if ns[it] == 0:
				del ns[it]
				del dn[it]
				del rn[it]
				nd -= 1
			if nd==0:
				break
			it = (it+1)%nd
	for row in range(nrc):
		for col in range(nrc):
			print(a[row][col],end=' ')
		print('\n')
