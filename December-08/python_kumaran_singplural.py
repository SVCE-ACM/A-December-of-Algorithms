

#python language
#getting a word from the user
string=input("Enter a string:")
n=input("Enter an integer:")

def plu(str1,n):
    #to print the singular form 
    if n=="1":
        new_str=str1[:-1]
        print(new_str)
    else:
        #adding "es" to the word
        if str1.endswith("sh") or str1.endswith ("ch") or str1.endswith("x") or str1.endswith("o"):
            print(str1+"es")
        #replacing f with ves    
        elif str1.endswith("f") or str1.endswith("fe"):
            print(str1.replace("f","v")+"es")
        #plural for words end with'y'    
        elif str1.endswith('y'):
            #for words which have vowel before 'y'
            if str1.endswith("ey") or str1.endswith("oy")or str1.endswith("uy") or str1.endswith("ay")or str1.endswith("iy"):
                print(str1+"s")
            else:
                #for words which have consonants before 'y' 
                str2=str1[:-1]+"ies"
                print(str2)
        #relacing us with i        
        elif str1.endswith("us"):
            str2=str1[:-2]+"i"
            print(str2)
        #replacing i with e    
        elif str1.endswith("is"):
            print(str1.replace("i","e"))
        #replacing 'on' with 'a'    
        elif str1.endswith("on"):
            print(str1.replace("on","a"))
        #adding 'es' to 's'    
        elif str1.endswith('s'):
            print(str1 + "es")
        #adding 's' for the other conditions    
        else:
            print(str1+"s")
            
            
plu(string,n)        
        

    
