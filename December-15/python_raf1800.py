def PT(n) :
    list=[1]
    xpow=n
    ypow=0
    yexp=n
    for i in range(n):
        print("".join(str(x)for x in list))
        newlist=[]
        newlist.append(list[0])
        for i in range(len(list)-1):
            newlist.append(list[i]+list[i+1])
        newlist.append(list[-1])
        list=newlist
    print("".join(str(x)for x in list))
    i=0
    print("Polynomial:")
    while(xpow>=0 and ypow<=n ):
        if xpow == 0:
            print("({}x^{}  * {}y^{})".format(list[i],xpow,yexp,ypow))
        else:            
            print("({}x^{}  * {}y^{})".format(list[i],xpow,yexp,ypow),end=' + ')
        xpow-=1
        ypow+=1
        yexp-=1
        i+=1
        
        
def main():
    x = int(input("Enter number of rows: "))
    PT(x);
    
if __name__ == "__main__":
    main()
