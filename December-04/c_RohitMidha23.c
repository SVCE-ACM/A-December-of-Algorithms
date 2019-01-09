#include<stdio.h> 
int fib(int n) 
{ 
    if (n <= 1) 
        return n; 
    return fib(n-1) + fib(n-2); 
} 

int main () 
{ 
    int n;
    printf("Enter value of n: "); 
    scanf("%d",&n); 
    printf("%d\n", fib(n+1));  
    //n+1 as fib(0) gives 0 but for user comfortability we make the 1st Fibonacci number as 0 
    return 0; 
} 
