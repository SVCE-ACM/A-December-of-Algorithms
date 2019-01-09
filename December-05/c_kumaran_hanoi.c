#include <stdio.h> 
  
// C recursive function to solve tower of hanoi puzzle 
void towerOfHanoi(int n, char from_rod[], char to_rod[], char aux_rod[]) 
{ 
    if (n == 1) 
    {
	cout<<"\n"<<from_rod<<to_rod;  
        return; 
    } 
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod);
    cout<<n<<from_rod<<to_rod;  
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod); 
} 
  
int main() 
{ 
    int n = 4; // Number of disks 
    towerOfHanoi(n, "left","middle","right");  // A, B and C are names of rods 
    return 0; 
} 
