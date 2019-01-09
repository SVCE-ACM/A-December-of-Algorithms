def caesar_cipher(c,s): 
	result = "" 
	for i in range(len(c)): 
		char = c[i] 
		if (char.isupper()): 
            # A is 65, a is 97. 
			result += chr((ord(char) + s-65) % 26 + 65) 
		else: 
			result += chr((ord(char) + s - 97) % 26 + 97) 

	return result 


c = input("Enter String to Encrypt : ")

s = int(input("Enter Cipher Value: "))

print ("Cipher: " + caesar_cipher(c,s))
