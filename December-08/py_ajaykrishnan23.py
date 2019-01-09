import inflect
import sys
a = inflect.engine()
def singularplural(s,n):
	if isinstance(n,int):
		if n in [-1,1]:
			if a.singular_noun(s) is False:
				print(s)
			else:
				print(a.singular_noun(s))
		else:
			if a.plural(s) is False:
				print(s)
			else:
				print(a.plural(s))
	elif isinstance(n,str):
			if n in s and n != s:
				print('Singular:',n)
				print('Plural:',s)
			elif s in n and n!= s:
				print('Singular:',s)
				print('Plural:',n)
			else:
				print('Invalid input')

s = sys.argv[1]
n = sys.argv[2]
if not n.isalpha():
	n = int(n)
singularplural(s,n)

