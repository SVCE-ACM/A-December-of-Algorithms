import sys
def base_condition(arr,min_length):
	temp = arr[0][:2]
	if(2<=min_length):
		for word in arr:
			if word[:2] != temp:
				return False
		return True 
	else:
		return False

arr = input('Enter strings in one line ').split()
min_length = None
for i in arr:
	if min_length is None or len(i)< min_length:
		min_length = len(i)
if(base_condition(arr,min_length)):
	print(arr[0][:2],end='')
else:
	print("No common prefix")
	sys.exit()

index=2
while(index<min_length):
	temp=arr[0][index]
	for word in arr:
		if word[index] != temp:
			sys.exit()
	else:
		print(temp,end='')
	index+=1
	
