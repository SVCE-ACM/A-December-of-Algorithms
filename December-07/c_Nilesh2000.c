# include <stdio.h>
void isApproximatelyEqual(float, float);
int main(void)
{
	float Num1, Num2;
	printf("\nInput Two Numbers : ");
	scanf("%f %f", &Num1, &Num2);
  isApproximatelyEqual(Num1, Num2);
	return 0;
}
void isApproximatelyEqual(float n1, float n2)
{
  int i, j;
  i=n1;
  j=n2;
   if(n1-i>0.5)
    i++;
   if(n2-j>0.5)
    j++;
   if(i==j)
    printf("They are approximately equal.\n");
   else
    printf("They are not approximately equal.\n");
}
