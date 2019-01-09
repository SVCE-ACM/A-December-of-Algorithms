#include <iostream>
using namespace std;
  
void func(int n) 
{ 
    int i, j = 1, k = 1; 
  
    // For each iteration increase j by 1 
    // and add it into k
    for (i = 1; i<n-1; i++) 
    {  
        j = j + 1; // Increasing j by 1 
        k = k + j; // Add value of j into k and update k 
    } 
    cout<<k;
} 
// Driven Function 
int main() 
{ 
    int n;
    cin>>n;
    func(n); 
    return 0; 
} 
