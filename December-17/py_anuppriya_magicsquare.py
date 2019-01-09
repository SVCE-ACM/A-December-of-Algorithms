def magicsq(n): 
    print("Order: 4 \nMagic sum: 34\n")  
    arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)] 
    for i in range(0,n//4): 
        for j in range(0,n//4): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
      
    for i in range(0,n//4): 
        for j in range(3 * (n//4),n): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
  
    for i in range(3 * (n//4),n): 
        for j in range(0,n//4): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
       
    for i in range(3 * (n//4),n): 
        for j in range(3 * (n//4),n): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
              
    for i in range(n//4,3 * (n//4)): 
        for j in range(n//4,3 * (n//4)): 
            arr[i][j] = (n*n + 1) - arr[i][j]; 
    print("Possible magic squares: ")    
    for i in range(n): #original
        for j in range(n):
            if((arr[i][j])%10)==arr[i][j]:
                print(arr[i][j],end="   ")
            else:
                print((arr[i][j]),end="  ") 
        print("",sep="\n")

    print("\n")
    for j in range(n): #original rev
        for i in range(n-1,-1,-1):
            if((arr[j][i])%10)==arr[j][i]:
                print(arr[j][i],end="   ")
            else:
                print((arr[j][i]),end="  ") 
        print("",sep="\n")

    print("\n")                    #down to top
    for i in range(n-1,-1,-1):
        for j in range(n):
            if((arr[i][j])%10)==arr[i][j]:
                print(arr[i][j],end="   ")
            else:
                print((arr[i][j]),end="  ") 
        print("",sep="\n")
        
    print("\n")
    #down to top reverse
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if((arr[i][j])%10)==arr[i][j]:
                print(arr[i][j],end="   ")
            else:
                print((arr[i][j]),end="  ") 
        print("",sep="\n")

    print("\n")
    for i in range(n):#transpose of orig
        for j in range(n):
            if((arr[j][i])%10)==arr[j][i]:
                print(arr[j][i],end="   ")
            else:
                print((arr[j][i]),end="  ") 
        print("",sep="\n") 

    print("\n")
    for j in range(n):#transpose of orig rev
        for i in range(n-1,-1,-1):
            if((arr[i][j])%10)==arr[i][j]:
                print(arr[i][j],end="   ")
            else:
                print((arr[i][j]),end="  ") 
        print("",sep="\n")     

    print("\n")
    for i in range(n-1,-1,-1):#transpose of down to top
        for j in range(n):
            if((arr[j][i])%10)==arr[j][i]:
                print(arr[j][i],end="   ")
            else:
                print((arr[j][i]),end="  ") 
        print("",sep="\n") 
    
    print("\n")
    #transpose of down to top rev
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if((arr[j][i])%10)==arr[j][i]:
                print(arr[j][i],end="   ")
            else:
                print((arr[j][i]),end="  ") 
        print("",sep="\n") 
    
    
n=4   
magicsq(n)  
