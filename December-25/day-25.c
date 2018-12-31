#include<stdio.h>

void main()
{
	char g[10][10];
	int i,j,m,n;
	int a,b;
	
	printf("Enter the santa's location:");
	scanf("%d %d",&i,&j);
	printf("Enter the childnlocation:");
	scanf("%d %d",&m,&n);
	
	g[i][j]='s';
	g[m][n]='c';
	
	for(a=0;a<10;a++)
	for(b=0;b<10;b++)
	{
		if(g[a][b]!='s'|| g[a][b]!='c')
		g[a][b]='*';
		
		
	}
	
		g[i][j]='s';
	g[m][n]='c';
	
	for(a=i+1;a<=m;a++)
	g[a][j]= "";
	
	for(b=j;b<n;b++)
	g[m][b]= "";
	


	for(a=0;a<10;a++)
	{
	printf("\n");
	for(b=0;b<10;b++)
	printf("\t%c",g[a][b]);}
	
	
	
}

