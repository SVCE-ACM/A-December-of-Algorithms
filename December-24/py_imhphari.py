def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 
  
s = input("Enter the string: ")
  
print ("The reversed string(using recursion) is : ") 
print (reverse(s)) 
