#include<iostream>
#include<string.h>

using namespace std;

int main()
{
    int a[10][10];
    int i,j,n=10, srci, srcj, desi, desj;
    
    cout<<"\nEnter start position:";
    cin>>srci>>srcj;
    cout<<"\nEnter end position:";
    cin>>desi>>desj;
    
    for(i=0;i<n;i++)
    {
        cout<<"\n";
        for(j=0;j<n;j++)
        {
            
            a[i][j]=42;
        }
    }
    
    for(i=srci;i<=desi;i++)
    {
        a[i][srcj]=32;
    }
    for(j=srcj;j<=desj;j++)
    {
        a[desi][j]=32;
    }
     for(i=0;i<n;i++)
    {
        cout<<"\n";
        for(j=0;j<n;j++)
        {
            
            cout<<char(a[i][j])<<" ";
        }
    }
    return 0;
}
