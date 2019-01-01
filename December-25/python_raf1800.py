def driver(sx,sy,cx,cy):
    mat={}
    mats=list()
    for i in range(10):
        for j in range(10):
                mat[i,j]='*'
    mat[sx,sy]='S'
    mat[cx,cy]='C'    
    csx=sx
    csy=sy
    while(csx!=cx or csy!=cy):
        if(csx<cx):
            csx+=1
            if(csx!=cx or csy!=cy):
                mat[csx,csy]='  ' 
        elif(csx>cx):
            csx-=1
            if(csx!=cx or csy!=cy):
                mat[csx,csy]='  '
        if(csy<cy):
            csy+=1
            if(csy!=cy or csy!=cy):
                mat[csx,csy]='  '
        elif(csy>cy):
            csy-=1
            if(csy!=cy or csy!=cy):            
                mat[csx,csy]='   '
    for i in mat.values():
        mats.append(i)
    pok=[mats[i:i+10] for i  in range(0,len(mats), 10)]
    for i in range(10):
        print(' '.join(pok[i]))
    
def main():
    x=input("Enter Santa's co-ordinates: ")
    x=x.split(',')
    x[0]=int(x[0])
    x[1]=int(x[1])
    y=input("Enter Child's co-ordinates: ")
    y=y.split(',')
    y[0]=int(y[0])
    y[1]=int(y[1])
    driver(x[0],x[1],y[0],y[1])
    
if __name__ == "__main__":
    main()

