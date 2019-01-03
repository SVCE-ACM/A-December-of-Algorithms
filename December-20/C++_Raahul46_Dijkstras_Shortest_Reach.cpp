#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""

#include <iostream>
#include <queue>
using namespace std;
int main()
{
	queue<int> q;
	
	int i,j,ne,nv,v,a[10][10],visited[10],dist[10],f,t,count,src,min=0;
	cout<<"Enter the number of vertices";
	cin>>nv;
	
	for(i=0;i<nv;i++)
		{
			visited[i]=0;
			dist[i]=100;
			for(j=0;j<nv;j++)
			{
				a[i][j]=100;
			}
		}
		
	cout<<"Enter the number of edges";
	cin>>ne;
	cout<<"\n Enter the edges one by one";
	for(i=0;i<ne;i++)
		{
			cout<<"\nFrom :";cin>>f;
			cout<<"\nTo :";cin>>t;
			cout<<"\n Enter the distance :";
			cin>>a[f][t];
			
		}
		
	cout<<"\n Distance Matrix:";
	for(i=0;i<nv;i++)
		{
			cout<<"\n";
			for(j=0;j<nv;j++)
			{
				cout<<a[i][j]<<"\t";
			}
		}
	cout<<"\n Enter the source vertex:";
	cin>>src;
	dist[src]=0;
	cout<<"\n Shortest Distance :";
	count=0;
	while(count<nv)
	{
		min=100;
		for(i=0;i<nv;i++)
			if(dist[i]<min && visited[i]==0)
				{
				v=i;
				min=dist[i];	
				}
		cout<<"\n Minimum distance vertex is:"<<v;
		visited[v]=1;
		count++;
		for(i=0;i<nv;i++)
		{
			if(((dist[v]+a[v][i])<dist[i]) && visited[i]==0)
			{
				dist[i]=dist[v]+a[v][i];			
			}
		}
	}
	cout<<"\n Calculated distances....";
	for(i=0;i<nv;i++)
	{
		cout<<"\n Vertex : "<<i<<"Distance : "<<dist[i];
	}	
	return 0;
}
