#include<stdio.h>
int main()
{
	int i,j,m,n,k,l;
	printf("Santa's location: ");
	scanf("%d%d",&n,&m);
	printf("Child's location: ");
	scanf("%d%d",&l,&k);
	for(i=0;i<10;i++)
	{
		printf("\n");
		for(j=0;j<10;j++)
		{
			if(i==m&&j==n)
			printf("S\t");
			else if(i==k&&j==l)
			printf("K\t");
			else if(((i==k&&(j>n&&j<l))||(j==n&&(i>m&&i<=k)))&&(m<k||n<l))
			printf(" \t");
			else if((i==m&&(j>l&&j<n))||(j==l&&(i>k&&i<=m)))
			printf(" \t");
			else
			printf("*\t");
		}
	}
	return 0;
}
