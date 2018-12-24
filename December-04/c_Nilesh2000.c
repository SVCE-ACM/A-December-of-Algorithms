# include <stdio.h>
double Fibonacci(int);
int main(void)
{
  int n;
  double Res;
  printf("\nEnter The Term To Be Printed...");
  scanf("%d", &n);
  Res=Fibonacci(n);
  printf("The %dth Term In The Fibonacci Series Is...%.0f\n", n, Res);
  return 0;
}
double Fibonacci(int n)
{
  int a=0, b=1;
  double c=0;
   if(n==1)
    return 0;
   for(int i=2;i<=n;i++)
    {
      a=b;
      b=c;
      c=a+b;
    }
  return c;
}
