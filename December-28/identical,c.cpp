#include<stdio.h>

void diag(int a[10][10],int r,int c)

{
	int s1=0,i,j;

		for(i=0;i<r-1;i++)
		for(j=i;j<c-1;j++)
		{
			if(a[i][j]==a[i+1][j+1])
			continue;
			else
			{
				s1=1;
				break;
			}
			
		}
		
		if(s1==1)
		printf("\nThe diagonals are not identical");
		else
			printf("\n The diagonals are  identical");
	
}



int main()
{
	int a[10][10];
	int r,c,i,j;
	printf("Enter the no.of rows and column:");
	scanf("%d %d",&r,&c);
	printf("\nEnter the Elements:");
	for(i=0;i<r;i++)
	for(j=0;j<c;j++)
	scanf("%d",&a[i][j]);
	diag(a,r,c);
	
	return 0;
}
