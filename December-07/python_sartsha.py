def IsApproximatelyEqual(a,b,t):
	if t.strip()=='':
		a = int(a+0.5)
		b = int(b+0.5)
		if a==b:
			return True
		else:
			return False
	else:
		t = float(t)
		diff = a-b
		if diff<0:
			diff = -1.0*diff
		if diff<=t:
			return True
		else:
			return False
a = float(input('Enter first number '))
b = float(input('Enter second number '))
th =input('Enter tolerance (leave empty if NA) ')
print(IsApproximatelyEqual(a,b,th))
