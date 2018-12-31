#include<stdio.h>
#include<string.h>

int main()
{
	char a[20][20];
	
	int n,i,j,c=0;
	
	printf("Enter the no.of Strings:");
	scanf("%d",&n);
	printf("\nEnter the strings:");
	for(i=0;i<n;i++)
	{
		 scanf(" %[^\n]",a[i]);
	
		
	}
	 	for(j=0;a[0][j]!='\0';j++)
    {
         for(i=0;i<n-1;i++)
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
return 0;    
}
	
