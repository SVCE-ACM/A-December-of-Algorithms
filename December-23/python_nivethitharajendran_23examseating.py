import numpy as np

def ExamSeats(nroom,nsize,ndepts,depts,depts2):
    c=1
    mat=[]
    mats = []
    i=0
    for x in range(nroom):
        s=nsize
        while s>0:
            if depts2[i][1]:
                mats.append(depts2[i][0]+str(c))
                depts2[i][1]-=1
            else:
                mats.append('__')
            i+=1
            if len(mats)==4:
                mat.append(mats.copy())
                mats.clear()
            if i==len(depts2):
                c+=1
                i=0
            s-=1
    T=mat.copy()
    for i in range(1, len(T), 2):
        T[i]=T[i][::-1]
    T1=list(np.array(T).flatten())
    c=1
    i=0
    while c<=nroom:
        print("Room {}".format(c))
        j=1
        for word in T1[i:i+nsize]:
            if j>4:
                print()
                j=1
            print(word, end="\t")
            j+=1
        i =nsize
        c+=1
        print("\n\n")
        

