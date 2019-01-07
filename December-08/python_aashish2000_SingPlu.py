import inflect
p=inflect.engine()

word, val=map(str, input().split())
print("SingularPlural(\""+word+"\",\""+str(val)+"\")")

flag=0
try:
	val=int(val)
except:
	flag=1

if flag==0:
	if (val==1) and (p.singular_noun(word) is False):
		print(word)
	elif (val>=2) and (((p.plural_noun(word)[-3:]=='ses' and p.plural_noun(word)[-4:]!='eses' and p.plural_noun(word)[-4:]!='uses') or (p.plural_noun(word)[-2:]=='ss')) or (p.plural_noun(word) is False)):
		print (word)
	elif (val==1) and (type(p.singular_noun(word)) == type('a')):
		print (p.singular_noun(word))
	elif (val>=2) and (type(p.plural_noun(word)) == type('a') ):
		print (p.plural_noun(word))
else:
	if (word in val):
		print ('Singular:', word)
		print ('Plural:', val)
	elif (val in word):
		print ('Singular:', val)
		print ('Plural:', word)
	else:
		print("Invalid Input")
