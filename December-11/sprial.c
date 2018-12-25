#include<stdio.h>

void main()
{
	int a[10][10],r,c,i,j,e=0;
	
	printf("Enter the no.of rows and columns in the matrix:");
	scanf("%d %d",&r,&c);
	
	printf("\nEnter the elements:\n");
	
	for(i=0;i<r;i++)
	for(j=0;j<c;j++)
	scanf("%d",&a[i][j]);
	
	while(e!=r*c)
	{
			for(i=0;i<r-2;i++)
        	for(j=0;j<c;j++)
        	{
			e++;
        	printf("%d--->",a[i][j]);}
	
	       for(i=r-2;i<r;i++)
	       for(j=c-1;j<c;j++)
	       {
		   e++;
	       	printf("%d--->",a[i][j]);
	       }
	       	
	       for(i=r-1;i<r;i++)
	       for(j=c-2;j>=0;j--)
	       {
		    e++;
	       	printf("%d--->",a[i][j]);
	}
	
	
	for(i=r-2;i<r-1;i++)
	       for(j=0;j<c-2;j++)
	       {
		   e++;
	       	printf("%d--->",a[i][j]);}
	       	
	       	for(i=1;i<2;i++)
	       for(j=1;j<2;j++)
	       {
		   e++;
	       	printf("%d--->",a[i][j]);}
	       	
	}
	
	
}
