import sys
vowels = {'a','e','i','o','u'}
def check(a):
	if a in vowels:
		return True
	else:
		return False

arr = input('Enter strings in one line\n').split()
m,n = len(arr),len(arr[0])
for i in range(m-1):
	for j in range(n-1):
		if(check(arr[i][j]) and check(arr[i+1][j]) and check(arr[i][j+1]) and check(arr[i+1][j+1])):
			print(str(i)+'-'+str(j))
			sys.exit()
print("Unavailable")
