#include<stdio.h>
void main()
{
	int m,n,i,j,a[10][10],k=0,l=0;
	printf("\n \t \t Enter the no. of rows and colums");
	scanf("%d %d",&m,&n);
	printf("\n \t \t Enter the elements ");
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{   scanf("%d",&a[i][j]);
	}
}
 while (k < m && l < n) 
    { 
        
        for (i = l; i < n; ++i) 
        { 
            printf("%d ", a[k][i]); 
        } 
        k++; 
  
        
        for (i = k; i < m; ++i) 
        { 
            printf("%d ", a[i][n-1]); 
        } 
        n--; 
  
        
        if ( k < m) 
        { 
            for (i = n-1; i >= l; --i) 
            { 
                printf("%d ", a[m-1][i]); 
            } 
            m--;
			 } 
  
        
        if (l < n) 
        { 
            for (i = m-1; i >= k; --i) 
            { 
                printf("%d ", a[i][l]); 
            } 
            l++;     
        }          	
	
}
}
