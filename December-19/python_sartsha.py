def simpleHash(s):
    l=[]
    for i in s:
        l.append(ord(i))
    b=sum(l)
    print(b/len(s))
s=input("Input: ")
simpleHash(s)
