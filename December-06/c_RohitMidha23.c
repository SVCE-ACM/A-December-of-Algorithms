#include<stdio.h>

int gcd(int a,int b)
{

    if (a == 0) 
        return b; 
    return gcd(b % a, a);
}
int findLCM(int arr[], int n) 
{  
    int result = arr[0]; 
   
    for (int i = 1; i < n; i++) 
        result = (((arr[i] * result)) / 
                (gcd(arr[i], result))); 
  
    return result; 
} 


int main()
{
    int a[10]; int n;
    printf("Enter number of elements: ");
    scanf("%d",&n);
    printf("\nEnter %d elements:  ",n);
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    printf("LCM is : %d\n",findLCM(a,n));
    return 0;
}