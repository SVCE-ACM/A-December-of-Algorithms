# include <stdio.h>
void isApproximatelyEqual(float, float, float);
int main(void)
{
	float Num1, Num2, thresholdLevel;
	printf("\nInput Two Numbers : ");
	scanf("%f %f", &Num1, &Num2);
  printf("Input Tolerance Level : ");
  scanf("%f", &thresholdLevel);
  isApproximatelyEqual(Num1, Num2, thresholdLevel);
	return 0;
}
void isApproximatelyEqual(float n1, float n2, float toleranceLevel)
{
  if(((n1-n2)<toleranceLevel && (n1>n2)) || ((n2-n1)<toleranceLevel && (n2>n1)))
	 printf("They are approximately equal.\n");
	else
	 printf("False as the difference is more than tolerance level.\n");
}
