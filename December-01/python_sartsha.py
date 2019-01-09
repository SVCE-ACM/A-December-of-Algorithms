def binarySearch(l,r):
	if(l<r):
		mid = l+(r-l)//2
		print('Guess',mid,arr[mid],'(half of',l,'to',str(r)+')','→ ',end='')
		if arr[mid] == key:
			print('spot on!')
			return 1
		elif(arr[mid]>key):
			print("you’re too high.")
			binarySearch(l,mid-1)
		elif(arr[mid]<key):
			print("you’re too low.")
			binarySearch(mid+1,r)
	else:
		return -1

arr = list(map(int,input().split()))
key = int(input())
ans = binarySearch(0,len(arr)-1)
if(ans==-1):
	print("Not found")


#input:	12 17 18 21 87 97 99 101 425 999
#	   	425
#output:Guess 4 87 (half of 0 to 9) → you’re too low.
#		Guess 7 101 (half of 5 to 9) → you’re too low.
#		Guess 8 425 (half of 8 to 9) → spot on!
