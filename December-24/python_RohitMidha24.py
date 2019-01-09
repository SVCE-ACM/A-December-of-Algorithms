def reverse(string): 
	if len(string) == 0: 
		return
	
	temp = string[0] 
	reverse(string[1:]) 
	print(temp, end='') 


string = input("Enter string : ")
reverse(string) 

