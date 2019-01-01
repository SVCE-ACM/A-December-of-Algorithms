def main():
	ip = input('Enter triangle one\'s sides and angles separated by commas')
	sna = ip.split(',')
	t1s = [int(x) for x in sna[:3]]
	t1a = [float(x) for x in sna[3:]]
	ip = input('Enter triangle two\'s sides and angles separated by commas')
	sna = ip.split(',')
	t2s = [int(x) for x in sna[:3]]
	t2a = [float(x) for x in sna[3:]]
	counts = 0
	counta = 0
	for a,b in zip(t1s,t2s):
		if a==b:
			counts = counts + 1
	for a,b in zip(t1a,t2a):
		if a==b:
			counta = counta + 1
	if counts == 3:
		print ('Triangles are similar by SSS')
	if counta == 3:
		print('Triangles are similar by AAA')
	if counts >=2 and counta == 1:
		print('Triangles are similar by SAS')
	if counts <3 and counta ==0:
		print('Triangles are\'nt similar')
		
main()