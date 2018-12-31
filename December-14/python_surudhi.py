def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s-97) % 26 + 97) 
  
    print('Encoded Output:',result)
s=int(input('Enter the key: '))
text=input('Enter the text: ')
print('Input:',text,s)
code=encrypt(text,s)

