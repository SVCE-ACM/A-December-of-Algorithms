def commonprefix(m):
    if not m: return ''
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1
m = [x for x in input('Enter the strings ').split()]
print('Strings:',m)
a=commonprefix(m)
if not a:
    print('No common prefix')
else:
    print('Common Prefix: ',a)
