#include<stdio.h>
#include<string.h>
void reverse(char *str) 
{ 
   if (*str) 
   { 
       reverse(str+1); 
       printf("%c",*str); 
    } 
} 
  

int main() 
{ 
   char a[10];
   printf("\n enter the new string");
   gets(a); 
   reverse(a); 
   return 0; 
} 
