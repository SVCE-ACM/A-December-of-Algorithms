def gcd(x,y):
	m = min(x,y)
	t = 1
	while(t <= m/2):
		if x%t == 0 and y%t == 0:
			sol = t
		t = t + 1
	return sol

x = int(input('Enter x'))
y = int(input('Enter y'))
sol = gcd(x,y)
print (sol)
lcm = x*y/sol
print('Lcm of the two inputs = ',lcm)