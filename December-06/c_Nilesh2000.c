# include <stdio.h>
int calcGCD(int x, int y)
{
  if(y==0)
   return x;
 return calcGCD(y, x%y);
}
void main()
{
  int Num1, Num2;
  printf("\nInput: ");
  scanf("%d %d",  &Num1, &Num2);
  int GCD=calcGCD(Num1, Num2);
  int LCM=(Num1*Num2)/GCD;
  printf("Output: %d\n", LCM);
}
