from os.path import commonprefix

lst=list(map(str, input().split()))
ans=(commonprefix(lst))
if len(ans)<=2:
	print("No common prefix")
else:
	print (ans)