
def aaa(a1, a2):              
    a1 = [float(i) for i in a1] 
    a2 = [float(i) for i in a2] 
    a1.sort() 
    a2.sort() 
      
    if a1[0] == a2[0] and a1[1] == a2[1] and a1[2] == a2[2]: 
        return 1
    return 0
  
def sas(s1, s2, a1, a2):  
      
    s1 = [float(i) for i in s1] 
    s2 = [float(i) for i in s2] 
    a1 = [float(i) for i in a1] 
    a2 = [float(i) for i in a2] 
      
    s1.sort() 
    s2.sort() 
    a1.sort() 
    a2.sort() 
      
    if s1[0] / s2[0] == s1[1] / s2[1]: 
        if a1[2] == a2[2]:          
            return 1
              
    if s1[1] / s2[1] == s1[2] / s2[2]: 
        if a1[0] == a2[0]: 
            return 1
              
    if s1[2] / s2[2] == s1[0] / s2[0]: 
        if a1[1] == a2[1]: 
            return 1
      
    return 0
  
def sss(s1, s2):  
      
    s1 = [float(i) for i in s1] 
    s2 = [float(i) for i in s2]  
    s1.sort() 
    s2.sort()  
      
    if(s1[0] / s2[0] == s1[1] / s2[1]  
        and s1[1] / s2[1] == s1[2] / s2[2]  
        and s1[2] / s2[2] == s1[0] / s2[0]): 
        return 1
      
    return 0
      
s1=[0]*3
s2=[0]*3
a1=[0]*3
a2=[0]*3  
for i in range(0,3):
  s1[i]=int(input("Enter sides for 1st Triangle: "))
for i in range(0,3):
  s2[i]=int(input("Enter sides for 2nd Triangle: ")) 
for i in range(0,3):
  a1[i]=int(input("Enter angles for 1st Triangle: "))   
for i in range(0,3):
  a2[i]=int(input("Enter angles for 2nd Triangle: "))
print("Sides 1:",s1,"Sides 2:",s2,"Angles 1:",a1,"Angles 2:",a2) 

aaa = aaa(a1, a2)  
sss = sss(s1, s2) 
sas = sas(s1, s2, a1, a2)  
if aaa or sss or sas:  
    print ("Triangles are similar by")
    if aaa: print ("AAA") 
    if sss: print ("SSS") 
    if sas: print ("SAS")
else: print ("Triangles are not similar")
             
