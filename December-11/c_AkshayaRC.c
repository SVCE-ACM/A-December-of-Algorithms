#include<stdio.h>
int main()
{
	int a[50][50],i,j,r,c;
	printf("enter the number of rows and columns: ");
	scanf("%d%d",&r,&c);
	printf("enter  elements of matrix\n");
	for(i=0;i<r;i++)
	{ for(j=0;j<c;j++)
		{
		  scanf("%d",&a[i][j]);
	  }
	}
	int l=0,m=r-1,p=0,q=c-1;
	printf("Matrix in spiral form:\n ");
	while(l<=m && p<=q)
	{
		for(i=p;i<=q;i++)
		{
			printf("%d  ",a[l][i]);
		}
		for(i=l+1;i<=m;i++)
		{
			printf("%d  ",a[i][q]);
		}
		for(i=q-1;i>=p;i--)
		{
			printf("%d  ",a[m][i]);
		}
		for(i=m-1;i>l;i--)
		{
				printf("%d  ",a[i][p]);
		}
		l++;
		m--;
		p++;
		q--;
	}
}
