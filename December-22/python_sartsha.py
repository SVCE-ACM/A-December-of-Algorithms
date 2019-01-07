def optional(counts):
	print('Top 20 words:')
	counts = dict(sorted(counts.items(),key =lambda a:a[1],reverse=True))
	count =0
	for i in counts:
		print(i+'\t'+ str(counts[i]))
		count+=1
		if(count==20):
			break

s = input('Enter string\n').lower()
words = sorted(s.split())
counts = {}
for word in words:
	counts[word] = counts.get(word,0) +1
for i in counts:
	print(i+'\t'+str(counts[i]))

optional(counts)


#input:Martha! Why did you say that name? Please! Stop! Why did you say that name?

#output:
"""
did     2
martha! 1
name?   2
please! 1
say     2
stop!   1
that    2
why     2
you     2
Top 20 words:
did     2
name?   2
say     2
that    2
why     2
you     2
martha! 1
please! 1
stop!   1
"""
