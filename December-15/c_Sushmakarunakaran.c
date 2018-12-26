#include <stdio.h>
 
int factorial(int n)
{  int c,result = 1;
   for (c = 1; c <= n; c++)
         result = result*c;
  return result;
}
 
int main()
{
   int i, n,j,a[50],x=0,y;
   printf("Enter the number of rows in pascal triangle\n");
   scanf("%d",&n);
   for (i = 0; i < n; i++)
   {
        for (j = 0 ; j<= i; j++)
        {
		y=(factorial(i)/(factorial(j)*factorial(i-j)));
        printf("%ld",y);
         if(i==n-1)
          {
		  a[x]=y;
		  x++;
	      }
        }
       printf("---> %d row",i); 
       printf("\n");
    }
   for(i=0,j=n-1;i<n,j>=0;i++,j--)
        printf("%d(x^%dy^%d)+",a[i],i,j);
return 0;
}
 

