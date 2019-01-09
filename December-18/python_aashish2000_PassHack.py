def allLexicographicRecur (string, data, last, index):
    global count 
    global l
    global flag
    if(flag==1):
        return
    length = len(string) 
    for i in range(length): 
        data[index] = string[i] 
  
        if index==last:
            count+=1
            #print(''.join(data)) 
            if(''.join(data)==l):
                flag=1
                return
        else: 
            allLexicographicRecur(string, data, last, index+1) 

def allLexicographic(string,size):
    length=size  
    data = [""] * (size) 
   
    string = sorted(string)
    allLexicographicRecur(string, data, length-1, 0)

flag=0
count=0
st=""
l=input("Enter Password: ")

for i in range(32,127):
    st=st+chr(i)

allLexicographic(st,len(l))

if(count/500000<=1.185926):
    print("Maximum time taken to brute-force:","Instantly")
else:
    print("Maximum time taken to brute-force:",count/500000, 'seconds' )


