#include<stdio.h>
int main()
{
	int i,j,a[7][7],m,n,flag=0;
	printf("Enter the no. of rows and columns ");
	scanf("%d%d",&m,&n);
	printf("Enter the elements ");
	for(i=0;i<m;i++)
	for(j=0;j<n;j++)
	scanf("%d",&a[i][j]);
	for(i=0;i<m-1;i++)
	for(j=0;j<n-1;j++)
	{
		if(a[i][j]==a[i+1][j+1])
		continue;
		else 
		{
			flag++;
			break;
		}
	}
	if(flag==0)
	printf("Identical diagonals");
	else
	printf("Diagonals are  non-identical");
	return 0;
}
