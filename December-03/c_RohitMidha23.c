#include<stdio.h>

int main()
{
    int n; 
    printf("Enter Ticket Number: ");
    scanf("%d",&n);
    int a[10];
    int temp=n,len=0;
    int rem; 
    while(temp>0)
    {
        a[len++] = temp%10;
        temp/=10;
    }
    int s1=0,s2=0;
    for(int i=0;i<len/2;i++)
        s1+=a[i];
    for(int i=len/2;i<len;i++)
        s2+=a[i];
    if(s2==s1)
        printf("For n = %d, isLucky(%d) = true\n",n,n);
    else 
        printf("For n = %d, isLucky(%d) = false\n",n,n);
    return 0;
}