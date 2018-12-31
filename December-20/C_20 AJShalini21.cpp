#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define INFINITY 9999
void dijkistra(int);
int a[10][10];
int main()
{
	int i,j,n;
	printf("Enter the no. of nodes: ");
	scanf("%d",&n);
	printf("Enter the matrix\n");
	for(i=0;i<n;i++)
    for(j=0;j<n;j++)
    scanf("%d",&a[i][j]);
    dijkistra(n);
	
	return 0;
}
void dijkistra(int n)
{
	int cost[10][10],dist[10],p[10],v[10];
	int c,min,nxt,i,j;
	for(i=0;i<n;i++)
	 for(j=0;j<n;j++)
       if(a[i][j]==0)
	   cost[i][j]=INFINITY;
	   else
	   cost[i][j]=a[i][j];
	for(i=0;i<n;i++)
	{
		dist[i]=cost[0][i];
		p[i]=0;
		v[i]=0;
	}
	dist[0]=0;
	v[0]=1;
	c=1;
	while(c<n-1)
	{
		min=INFINITY;
		for(i=0;i<n;i++)
		if(dist[i]<min&&v[i]!=1)
		{
			min=dist[i];
			nxt=i;
		}
		v[nxt]=1;
		for(i=0;i<n;i++)
		    if(i!=0&&i!=nxt)
	            if(min+cost[nxt][i]<dist[i])
	            {
	            	dist[i]=min+cost[nxt][i];
	            	p[i]=nxt;
				}
		c++;
	}
	printf("Vertex   Distance from source");
	for(i=0;i<n;i++)
	    printf("\n%d\t%d",i,dist[i]);
}
