#include<stdio.h>
void main()
{
	int a[10][10],i,j,r,c,x,y=1;
	printf("\n enter the number of rows and columns");
	scanf("%d %d",&r,&c);
	printf("\n enter the elements");
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		   scanf("%d",&a[i][j]);
	}
	x=a[0][0];
	for(i=1;i<r;i++)
	{
		if(a[i][i]==x)
		  y++;
	}
	if(y==r)
	  printf("\n \t YEAH!! diagonal elements are identical");
	else
	  printf("\n \t NOPE! diagonal elements are not identical");  
}
