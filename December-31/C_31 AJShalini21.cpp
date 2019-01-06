#include<stdio.h>
int main()
{
	int a[5][5],i,j,r,c,m,n,x,y,s=99;
	printf("\nEnter the no. of rows and columns ");
	scanf("%d %d",&r,&c);
	printf("Enter the elements containing only 0's,2's and single 1 ");
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			scanf("%d",&a[i][j]);
			if(a[i][j]==1)
			{
				m=i;
				n=j;
			}
		}
	}
	x=m;
	y=n;
	for(i=1,j=1;i<r,j<c;i++,j++)
	{
		m=(x+i)%r;
		if(a[m][y]==2)
		{
			if(m>x&&s>i)
			s=i;
			else if(x>m&&s>(x-m))
			s=x-m;
			else
			continue;
		}
		n=(y+j)%c;
		if(a[x][n]==2)
		{
		    if(n>y&&s>i)
			s=i;
			else if(y>n&&s>(y-n))
			s=y-n;
			else
			continue;
	    }
	}
	printf("The distance of nearest 2 from 1 is %d ",s);
	return 0;
}
