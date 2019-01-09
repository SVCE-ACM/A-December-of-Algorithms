
// C++ program to check if a given number is lucky 
#include<iostream> 
using namespace std; 
  
// This function returns true if n is lucky 
bool isLucky(int n) 
{ 
    // Create an array of size 10 and initialize all 
    // elements as false. This array is used to check 
    // if a digit is already seen or not. 
    bool arr[10]; 
    for (int i=0; i<10; i++) 
        arr[i] = false; 
  
    // Traverse through all digits of given number 
    while (n > 0) 
    { 
        // Find the last digit 
        int digit = n%10; 
  
        // If digit is already seen, return false 
        if (arr[digit]) 
           return false; 
  
        // Mark this digit as seen 
        arr[digit] = true; 
  
        // REmove the last digit from number 
        n = n/10; 
    } 
    return true; 
} 
  
// Driver program to test above function. 
int main() 
{ 
    int arr[] = {1291, 897, 4566, 1232, 80, 700}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
  
    for (int i=0; i<n; i++) 
        isLucky(arr[i])? cout << arr[i] << " is Lucky \n": 
                         cout << arr[i] << " is not Lucky \n"; 
    return 0; 
}
