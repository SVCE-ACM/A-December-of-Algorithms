import re
s=input()
w=s.find(',')
v='[aeiou]'*2
m=re.search(v+'.'*~-w+v,s)
print (m and divmod(m.start(),-~w) or 'not found')
