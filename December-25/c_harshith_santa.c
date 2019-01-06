#include<stdio.h>
void main()
{
	char a[12][12];
	int i,j,s1,s2,c1,c2;
	
	for(i=1;i<11;i++)
	{
		for(j=1;j<11;j++)
		  a[i][j]='*';
	}
	printf("\nenter santa's position");
	scanf("%d %d",&s1,&s2);
	printf("\nenter child's position");
	scanf("%d %d",&c1,&c2);
	a[c1][c2]='c';
	a[s1][s2]='s';
	for(i=s2+1;i<=c2;i++)
	 a[s1][i]=' ';
	for(i=s1+1;i<c1;i++)
	 a[i][c2]=' ';
		for(i=0;i<12;i++)
	{
		for(j=0;j<12;j++)
		{
		    printf("%c",a[i][j]);
		   
	    }
	printf("\n");	  
    }
}
