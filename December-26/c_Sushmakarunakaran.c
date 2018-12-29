#include<stdio.h>
void main()
{
	char a[10][10];
	int i,j,r,c=0;
	printf("\n enter the no. of strings");
	scanf("%d",&r);
	printf("\n enter the strings");
		for(i=0;i<r;i++)
	      scanf("%s",a[i]);
	      
    	for(j=0;a[0][j]!='\0';j++)
    {
         for(i=0;i<r-1;i++)
    	{
    		if(a[i][j]==a[i+1][j])
    		
			 	continue;
			 
			 else
			 {  c++;
			    break;
			 }
		}
		if(c!=0)
		 break;
	}
	if(j<2)
	 printf("\n no common prefix");
	else
	{  printf("\n common string:");
	  for(i=0;i<j;i++)
	   printf("%c",a[0][i]);
    }
    
}
