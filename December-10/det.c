#include<stdio.h>

void main()
{
	int a[10][10],r,c,i,j,d;
	
	printf("Enter the no:of Rows and Columns in matrix:");
	scanf("%d %d",&r,&c);	
	
	if (r!=c)
	{
		printf("\nThe determintant cannot be found:");
	}
	else if( r==2)
	{
			printf("\nEnter the elements in the array:\n");
			for(i=0;i<2;i++)
			for(j=0;j<2;j++)
			scanf("%d",&a[i][j]);
			
			d=(a[0][0] * a[1][1]) - (a[0][1] *a[1][0]);
	        printf("The value of determintant is :%d",d);		
		}
	else if(r==3)
	{
			printf("\nEnter the elements in the array:\n");
			for(i=0;i<3;i++)
			for(j=0;j<3;j++)
			scanf("%d",&a[i][j]);
			
			d=((a[0][0])*(a[1][1]*a[2][2] - a[1][2]*a[2][1]) - (a[0][1])*(a[1][0]*a[2][2] - a[1][2]*a[2][0]) + (a[0][2])*(a[1][0]*a[2][1] - a[1][1]*a[2][0]));
		printf("The value of determintant is :%d",d);	
			}		

}
