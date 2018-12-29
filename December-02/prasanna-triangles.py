a1=[80,60,40]
a2=[40,60,80]
s1=[2,3,3]
s2=[4,6,6]
def sssrule(s1,s2):
    s1.sort()
    s2.sort()
    if s1[0]//s2[0]==s1[1]//s2[1]==s1[2]//s2[2]:
        return True
    else:
        return False
def sasrule(s1,s2,a1,a2):
    a1.sort()
    a2.sort()
    s1.sort()
    s2.sort()
    if s1[0]//s2[0]==s1[1]//s2[1] and a1[0]==a2[0]:
        return True
    
    if s1[1]//s2[1]==s1[2]//s2[2] and a1[1]==a2[1]:
        return True
    
    if s1[2]//s2[2]==s1[1]//s2[1] and a1[2]==a2[2]:
        return True
    else:
        return False
def aarule(a1,a2):
    a1.sort()
    a2.sort()
    if a1[2]==a2[1] and a1[2]==a2[2] and a1[0]==a2[0]:
        return True
    else:
        return False
    
sss=sssrule(s1,s2)
sas=sasrule(s1,s2,a1,a2)
aa=aarule(a1,a2)
if sss or sas or aa:
    
    print("side1=[",s1[0],s1[1],s1[2],"] angle1=[",a1[0],a1[1],a1[2],"]")
    print("side2=[",s2[0],s2[1],s2[2],"] angle2=[",a2[0],a2[1],a2[2],"]")
    if sss:
      print("triangles are similiar by SSS")
    if sas:
      print("triangles are similiar by SAS")
    if aa:
      print("triangles are similiar by AA")
else:
    print("TRIANGLES ARE DISIMMILAR")