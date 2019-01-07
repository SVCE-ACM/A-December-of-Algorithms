def fun_aaa(angle1,angle2):
    angle1.sort()
    angle2.sort()
    if angle1[0]==angle2[0] and angle1[1]==angle2[1] and angle1[2]==angle2[2]:
        return 1
    else:
        return 0
def fun_sas(side1,side2,angle1,angle2):
    side1.sort()
    side2.sort()
    angle1.sort()
    angle2.sort()
    if side1[0]//side2[0] == side1[1]//side2[1]:
        if angle1[2]==angle2[2]:
            return 1
    if side1[1]//side2[1] == side1[2]//side2[2]:
        if angle1[0]==angle2[0]:
            return 1
    if side1[2]//side2[2] == side1[0]//side2[0]:
        if angle1[1]==angle2[1]:
            return 1
    return 0
def fun_sss(side1,side2):
    side1.sort()
    side2.sort()
    if(side1[0]//side2[0]==side1[1]//side2[1] and side1[1]//side2[1]==side1[2]//side2[2] and side1[2]//side2[2]==side1[0]//side2[0]):
        return 1
    else:
        return 0
side1=[2,3,3]
side2=[4,6,6]
angle1=[80,60,40]
angle2=[40,60,80]
aaa=fun_aaa(angle1,angle2)
sas=fun_sas(side1,side2,angle1,angle2)
sss=fun_sss(side1,side2) 
if  aaa == 1 and sas == 1 and sss == 1:
    print("The traingles are equal by AAA,SAS,SSS rule")
else:
    print("The traingles are not equal")


    
    
    
    

