def strrev(s,i,count):
	s[i],s[len(s)-1-i] = s[len(s)-1-i],s[i]
	i += 1
	count=count+1
	print(s)
	if count<len(s)/2:
		strrev(s,i,count)
	else:
		print(''.join(s))
	
s = input('enter string')
strrev(list(s),0,0)
