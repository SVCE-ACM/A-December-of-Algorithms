def findpre(s):
	pre = s[0][0]+s[0][1]
	i = 2
	p = 0
	while(i<=len(s[0])):
		count = 0
		for string in s:
			f = 0
			if pre == string[0:i]:
				count += 1
				f = 1
			else:
				if f==0 and p == 0:
					print('No common prefix')

				else:
					print('Common prefix : ' + pre[0:len(pre)-1])
				exit()
				
		if count == len(s):
			i += 1
			p = 1
			pre = s[0][0:i]
	if f!=0:
		print('Common prefix :' + pre)
	
s = input('enter strings separated by \',\'')
s = list(s.split(','))
s = sorted(s,key=len)
findpre(s)
