def isLucky(n):
	l = len(n)//2
	if (sum(map(int,n[:l])) == sum(map(int,n[l:]))):
		return True
	else:
		return False
n = input()
print(isLucky(n))

#input:1230
#output:True
