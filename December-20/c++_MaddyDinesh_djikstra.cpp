
#include<iostream> 
using namespace std;
void Dijkstra();
void read(); 
void print();
int n, source, cost[10][10], dist[10];
main()
 {
read();
Dijkstra();
cout<<"The Shortest Path :: ";
 print();
 }
void read() 
{
int i,j;
cout<<"Enter the number of nodes :: ";
 cin>>n;
cout<<"Enter the cost matrix ::\n";
 for(i = 1;i <= n; i++) 
{
for(j = 1; j <= n; j++) 
{
cout<<"cost["<<i<<"]["<<j<<"] :: ";
 cin>>cost[i][j];
 if(cost[i][j] == 0)
cost[i][j] = 999;
 }
 }
cout<<"Enter the source matrix:"; 
cin>>source;
 }
void Dijkstra() 
{
int u, v = source, w, count, flag[10], min, i;
for(i=1;i<=n;i++)
{
flag[i]=0; 
dist[i]=cost[v][i];
 }
 count=2;
 while(count<=n) 
{
min=99; 
for(w=1;w<=n;w++) 
{
if(min > dist[w] && !flag[w]) 
{
min=dist[w]; 
u=w; 
} 
}
flag[u]=1;
 count++;
for(w=1;w<=n;w++)
if((dist[w]>dist[u]+cost[u][w]) && !flag[w])
dist[w]=dist[u]+cost[u][w]; 
}
 }
void print() 
{
int i;
 for(i=1;i<=n;i++)
 if(i!=source)
cout<<"\n"<<source<<"->"<<i<<"="<<dist[i];
}

