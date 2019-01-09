num=input("ENTER STRINGS:")
a=num.split()

prefix_len = len(a[0])
for x in a[1 : ]:
    prefix_len = min(prefix_len, len(x))
    while not x.startswith(a[0][ : prefix_len]):
        prefix_len -= 1

prefix = a[0][ : prefix_len]
print(prefix)
