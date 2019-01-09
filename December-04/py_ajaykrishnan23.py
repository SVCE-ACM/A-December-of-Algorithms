def fibo(n):
	t = 0
	a = 0
	b = 1

	while(t<n):
		if t == n-1:
			print ('N\'th term is '+str(a))
		c = a + b
		a = b
		b = c
		t= t+1

def main():
	n = int(input('Upto which term?'))
	fibo(n)

main()