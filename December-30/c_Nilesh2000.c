# include <stdio.h>
int main(void)
{
  int n;
  printf("\nInput : ");
  scanf("%d", &n);
  int Diagonals=(n*(n-3))/2;
  printf("Output : %d\n", Diagonals);
  return 0;
}
