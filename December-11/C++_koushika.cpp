#include <iostream>
using namespace std;
  
void spiralPrint(int m, int n, int mat[30][30]) 
{ 
    int i, k = 0, l = 0; 
  
    while (k < m && l < n) 
    { 
        
        for (i = l; i < n; ++i) 
        { 
            cout<<mat[k][i]<<" --> "; 
        } 
        k++; 
  
    
        for (i = k; i < m; ++i) 
        { 
            cout<<mat[i][n-1]<<" --> ";
        } 
        n--; 
  
        if ( k < m) 
        { 
            for (i = n-1; i >= l; --i) 
            { 
                cout<<mat[m-1][i]<<" --> "; 
            } 
            m--; 
        } 
        
        if (l < n) 
        { 
            for (i = m-1; i >= k; --i) 
            { 
                cout<<mat[i][l]<<" --> "; 
            } 
            l++;     
        }         
    } 
} 
  
/* Driver program to test above functions */
int main() 
{ 
    int i,j,r,c, mat[30][30];
    cout<<"\nEnter row and column of matrix:";
    cin>>r>>c;
    cout<<"\nEnter elements of matrix:";
    for(i=0;i<r;i++)
    for(j=0;j<c;j++)
    cin>>mat[i][j];
    spiralPrint(r,c, mat); 
    return 0; 
} 
