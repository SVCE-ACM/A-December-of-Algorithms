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
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			if(i==Santa.x && j==Santa.y)
			 Mat[i][j]='S';
			else if(i==Child.x && j==Child.y)
			 Mat[i][j]='K';
			else if(i>=Santa.x+1 && i<Child.x+1)
			 Mat[i][Santa.y]=' ';
			else if(j>=Santa.y+1 && j<Child.y)
			 Mat[Child.x][j]=' ';
			else
			 Mat[i][j]='*';
			printf("%c ", Mat[i][j]);
		}
	 printf("\n");
	}
	return 0;
}
