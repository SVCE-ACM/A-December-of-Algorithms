from collections import Counter
file=open('text.txt', 'r')
all_words=(file.read().split())
file.close()
count=dict(Counter(all_words))
keys=list(count.keys())
allw=[]
for word in keys:
	allw.append([word, count[word]])
for w in range(len(allw)):
	allw[w][0]=allw[w][0].lower()
allw.sort()
for i in allw:
	print (' '.join(map(str,i)))