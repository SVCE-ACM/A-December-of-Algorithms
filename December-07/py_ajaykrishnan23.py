import math
def isapproximatelyequal(x,y):
	if '.' in str(x):
		x = x + 0.5
		if(y == math.floor(x)):
			print('True')
			return True
		else:
			print('False')
			return False
	else:
		x = x + 5
		if y == x*(x/10):
			print('True')
			return True
		else:
			print('False')
			return False

#with tolerance

def isapproximatelyequalwtol(x,y,tol):
	if abs(x-y) <= tol:
		print('True')
		return True
	else:
		print('False')
		return False
		
x = float(input('Enter x'))
y = float(input('Enter y'))
tol = float(input('Enter tolerance'))

sol = isapproximatelyequal(x,y)
sol = isapproximatelyequalwtol(x,y,tol)