def spiral(m,n,a) : 
    k=0
    l=0
 
    while (k < m and l < n): 
        for i in range(l,n): 
            print(a[k][i],end = " ")          
        k+=1
  
        for i in range(k,m): 
            print(a[i][n-1],end=" ") 
              
        n -=1

        if ( k < m) :  
            for i in range(n-1,(l-1),-1) : 
                print(a[m - 1][i],end=" ") 
              
            m-=1
          
        if(l<n): 
            for i in range(m-1,k-1,-1): 
                print(a[i][l],end=" ") 
              
            l+=1
  
a=[[1,2,3],[4,5,6],[7,8,9]] 
        
r=3
c=3
spiral(r,c,a) 
