#include<stdio.h>
#include<iostream>
#include<stdlib.h>

using namespace std;
  
/* Function to print reverse of the passed string */
void reverse(char *str) 
{ 
   if (*str) 
   { 
       reverse(str+1); 
       cout<<*str; 
   } 
} 
  
/* Driver program to test above function */
int main() 
{ 
   char a[100];
   cout<<"\nEnter a string:";
   gets(a);
   reverse(a); 
   return 0; 
}
