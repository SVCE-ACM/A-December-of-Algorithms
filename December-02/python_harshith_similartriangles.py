def simi_aaa(a1, a2):              
    a1.sort() 
    a2.sort() 
      
    if a1[0] == a2[0] and a1[1] == a2[1] and a1[2] == a2[2]: 
        return 1
    return 0

def simi_sas(s1, s2, a1, a2):  
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
  
def simi_sss(s1, s2):  
    s1.sort() 
    s2.sort()  
    if(s1[0] / s2[0] == s1[1] / s2[1]  
        and s1[1] / s2[1] == s1[2] / s2[2]  
        and s1[2] / s2[2] == s1[0] / s2[0]): 
        return 1
      
    return 0
 
s1 = [2,3,3]
s2 = [4,6,6]
          
a1 = [80,60,40]
a2 = [40,60,80]

aaa = simi_aaa(a1, a2)  
sss = simi_sss(s1, s2)  
sas = simi_sas(s1, s2, a1, a2)   
if aaa or sss or sas:  
    print ("Triangles are similar by"), 
    if aaa: print ("AAA"),  
    if sss: print ("SSS"),  
    if sas: print ("SAS")
else: 
  print ("Triangles are not similar")
