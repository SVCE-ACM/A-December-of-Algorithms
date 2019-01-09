lst=[]
def permute(s,i,n):
    if i==n:
       lst.append(''.join(s))
    else:
        for j in range(i,len(s)):
            s[i],s[j]=s[j],s[i]
            permute(s,i+1,n)
            s[i],s[j]=s[j],s[i]
def main():
    st=input("Input:")
    a=list(st)
    print("Posible combinations:")
    permute(a,0,len(st)-1)
    lst.sort()
    #print(lst)
    print('\n'.join(lst))
    for i in lst:
        if i==st:
            print("Match at position",lst.index(i)+1)
main()
