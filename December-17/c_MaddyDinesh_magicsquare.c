#include<stdio.h>
#include<conio.h>
void generateSquare(int n) 
{ 
    int magicSquare[n][n]; 
    int num;
  
   
    memset(magicSquare, 0, sizeof(magicSquare)); 
  
    
    int i = n/2; 
    int j = n-1; 
  
  
	
for ( num=1; num <= n*n; ) 
    { 
        if (i==-1 && j==n) 
        { 
            j = n-2; 
            i = 0; 
        } 
        else
        { 
            
            if (j == n) 
                j = 0; 
  
           
            if (i < 0) 
                i=n-1; 
        } 
        if (magicSquare[i][j])  
        { 
            j -= 2; 
            i++; 
            continue; 
        } 
        else
            magicSquare[i][j] = num++;  
  
        j++; i--;  
    } 
  
printf("The Magic Square for n=%d:\nSum of "
       "each row or column :%d\n\n",  n, n*(n*n+1)/2); 
    for (i=0; i<n; i++) 
    { 
        for (j=0; j<n; j++) 
            printf("%3d ", magicSquare[i][j]); 
        printf("\n"); 
    } 
} 
  

int main() 
{ 
    int n;
    printf("Enter the number:"); // Works only when n is odd
	scanf("%d",&n); 
    generateSquare (n); 
    return 0; 
} 
