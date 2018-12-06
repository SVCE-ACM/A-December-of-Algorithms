                                      // (Binary search)
#include<stdio.h>
void main()
{
int s,g;	
printf("Say my chosen number is :");
scanf("%d",&s);
while(1)
{
printf("\n\nGuess:");
scanf("%d",&g);
if(s==g)
{
	printf("\nSpot ON !!!");
	break;
}
else if(s>g)
	printf("\nyou are too low.");
else
	printf("\nyou are too high");	
}
}
