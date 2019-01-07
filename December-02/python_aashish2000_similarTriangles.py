def sss_simi(s1,s2):
    s1.sort()
    s2.sort()
    if((s1[0]/s2[0])==(s1[1]/s2[1]) and (s1[0]/s2[0])==(s1[2]/s2[2])):
        return(1)
    return(0)

def sas_simi(s1,s2,a1,a2):
    if((s1[0]/s2[0])==(s1[1]/s2[1]) and (a1[0]==a2[0])):
        return(1)
    elif((s1[2]/s2[2])==(s1[1]/s2[1]) and (a1[1]==a2[1])):
        return(1)
    elif((s1[0]/s2[0])==(s1[2]/s2[2]) and (a1[2]==a2[2])):
        return(1)
    return(0)

def aaa_simi(a1,a2):
    a1.sort()
    a2.sort()
    if((a1[0]==a2[0]) and (a1[1]==a2[1]) and (a1[2]==a2[2])):
        return(1)
    else:
        return(0)


s1=list(map(int,input("Sides of Triangle 1: ").split()))
s2=list(map(int,input("Sides of Triangle 2: ").split()))
a1=list(map(int,input("Angles of Triangle 1: ").split()))
a2=list(map(int,input("Angles of Triangle 2: ").split()))

aaa=aaa_simi(a1,a2)
sss=sss_simi(s1,s2)
sas=sas_simi(s1,s2,a1,a2)

if aaa or sss or sas:     
    print("Triangles are similar by",end=" ")     
    if aaa: print("AAA",end=" ")     
    if sss: print("SSS",end=" ") 
    if sas: print("SAS")
else:
    print("Triangles are not Similar")


 
