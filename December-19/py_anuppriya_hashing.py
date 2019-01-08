def simpleHash(string):
    s=0
    s1=0
    for i in string:
        ch=ord(i)
        s=s+ch  
    while(s!=0):
       x=s%10
       s1+=x
       s=s//10
    return s1
string=input("Enter a string")
print(simpleHash(string))
