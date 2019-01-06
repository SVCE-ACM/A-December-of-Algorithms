side1=s1=angle1=a1=[]
sss=sas=aaa=0
side2=s2=angle2=a2=[]
side1=sorted(input("enter sides of triangle1 (seperated by comma)").split(","))
s1=[int(i) for i in side1]
side2=sorted(input("enter sides of triangle2").split(","))
s2=[int(i) for i in side2]
angle1=sorted(input("enter angles of triangle1").split(","))
a1=[int(i) for i in angle1]
angle2=sorted(input("enter angles of triangle2").split(","))
a2=[int(i) for i in angle2]
if s1[0]/s2[0]==s1[1]/s2[1]==s1[2]/s2[2]:
    sss=1
if((s1[0]/s2[0]==s1[1]/s2[1]) and a1[2]==a2[2]) or (s1[1]/s2[1]==s1[2]/s2[2] and a1[0]==a2[0]) or (s1[2]/s2[2]==s1[0]/s2[0] and a1[1]==a2[1]):
    sas=1
if a1[0]==a2[0] and a1[1]==a2[1] and a1[2]==a2[2]:
    aaa=1
if sss==1 or sas==1 or aaa==1:
    print("\nThe triangles are similar by ")
    if sss==1:
        print("SSS")
    if sas==1:
        print("SAS")
    if aaa==1:
        print("AAA")
else:
    print("The triangles are not similar")
    
