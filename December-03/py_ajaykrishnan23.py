def islucky(n):
	count = 0
	t = n
	while(t>0):
		t = int(t/10)
		count = count+1
	t = 0
	l = 0
	r = 0
	while(t < count/2):
		rem = n%10
		r = r + rem
		t = t + 1
		n = int(n/10)
	while(t < count):
		rem = n%10
		l = l + rem
		t = t + 1
		n = int(n/10)
	if l==r:
		return True
	else:
		return False
		
def main():
	n = int(input('Enter a Ticket number'))
	k = islucky(n)
	print(k)

main()