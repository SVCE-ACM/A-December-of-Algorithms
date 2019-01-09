def hcf(a,b):
	while (a!=b):
		if a<b:
			b-=a
		else:
			a-=b
	return a
def findlcm(arr):
	lcm = arr[0]
	for i in arr[1:]:
		lcm = lcm*i/hcf(lcm,i)
	return int(lcm)

arr = list(map(int,input("Enter numbers: ").split(',')))
print(findlcm(arr))

#Enter numbers: 2, 3, 6, 12, 24, 64
#output:192
