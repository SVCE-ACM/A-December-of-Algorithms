# include <stdio.h>
struct Position
{
	int x;
	int y;
};
int main(void)
{
  struct Position Santa, Child;
	char Mat[10][10];
	printf("\nSanta's Location: ");
	scanf("%d %d", &Santa.x, &Santa.y);
	printf("Child's Location: ");
	scanf("%d %d", &Child.x, &Child.y);
	printf("\n*");
	for(int Iter=0;Iter<10;Iter++)
	 printf(" %d", Iter);
	for(int i=0;i<10;i++)
	{
	 printf("\n%d ", i);
		for(int j=0;j<10;j++)
		{
			if(i==Santa.y && j==Santa.x)
			 printf("S ");
			else if(i==Child.y && j==Child.x)
			 printf("K ");
			else if((i==Santa.y && (j>Child.x && j<Santa.x)) || (i==Child.y && (j>Santa.x && j<Child.x)) && (Santa.y<Child.y || Santa.x< Child.x))
			 printf("  ");
			else if((j==Santa.x && (i>Santa.y && i<=Child.y)) || (j==Child.x && (i>Child.y && i<=Santa.y)))
			 printf("  ");
			else
			 printf("* ");
		}
  }
	printf("\n");
	return 0;
}
