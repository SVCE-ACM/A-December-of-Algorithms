#include <iostream> 
using namespace std; 
  
// C++ function to find number of diagonals 
// in n sided convex polygon 
int numberOfDiagonals(int n) 
{ 
    return n * (n - 3) / 2; 
} 
  
// driver code to test above function 
int main() 
{ 
    int n ; 
    cin>>n ; 
    cout << numberOfDiagonals(n) << " diagonals"; 
    return 0; 
} 
