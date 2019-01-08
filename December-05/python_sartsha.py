def Hanoi(n,frm='left',mid='middle',to='right'):
	if(n>0):
		Hanoi(n-1,frm,to,mid)
		print(frm+"=>"+to)
		Hanoi(n-1,mid,frm,to)

n =  int(input('Number of disks: '))
Hanoi(n)
