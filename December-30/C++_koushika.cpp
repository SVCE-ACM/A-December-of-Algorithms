#include <iostream> 
using namespace std; 
  
int numberOfDiagonals(int n) 
{ 
    return n * (n - 3) / 2; 
} 
  
int main() 
{ 
    int n = 5; 
    cout << n << " sided polygon has "; 
    cout << numberOfDiagonals(n) << " diagonals"; 
    return 0; 
} 
