def spiral(m,r,c,ch,itr,itc):
	if itr<r and itc<c:	
		if ch == 1:
			for i in range(itc,c):
				print(m[itr][i],'-->',end='')
			itr += 1
			
			for j in range(itr,r):
				print(m[j][i],'-->',end='')
			c-= 1
			spiral(m,r,c,-1,itr,itc)
		
		if ch == -1:
			for i in range(c-1,itc-1,-1):
				print(m[r-1][i],'-->',end='')
			r -= 1
			for j in range(r-1,itr-1,-1):
				print(m[j][i],'-->',end='')
			itc += 1
			spiral(m,r,c,1,itr,itc)


r1 = int(input('Enter number of rows of m1'))
c1 = int(input('Enter number of coloumns of m1'))
m1 = [ [0 for i in range(0,c1)] for j in range(0,r1)]
print('Enter matrix 1')
for i in range(0,r1):
	for j in range(0,c1):
		m1[i][j] = int(input('Enter element'))
spiral(m1,r1,c1,1,0,0)