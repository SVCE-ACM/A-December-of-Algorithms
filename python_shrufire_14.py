x1=input('Input:')
str=[]
for i in range(len(x1)-2):
    char=x1[i]    
    ch=chr(ord(char)+int(x1[-1]))
    str.append(ch)
x=''.join(str)
print('Encoded Output:',x)


