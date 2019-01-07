import string
import hashlib

s=input("Enter String: ")
ans=int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % 10**8
newans=str(ans)
while(len(newans)!=8):
	newans="0"+newans
print(newans)

