# include <stdio.h>
int main(void)
{
  int n;
  printf("\nInput : ");
  scanf("%d", &n);
  int Res=(n*(n-1))/2;
  printf("Output : %d\n", Res);
  return 0;
}
