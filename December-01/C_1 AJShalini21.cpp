#include<stdio.h>
int main()
{
	int n=100,key,guess,low=0,mid,high;
	printf("Say my choosen number is\t");
	scanf("%d",&key);
	high=n;
	while(low<=high)
	{
		printf("\nGuess\t");
		scanf("%d",&guess);
		mid=(low+high)/2;
		if(key==guess)
		{
			printf("half of %d to %d -> spot on",low,high);
			break;
		}
		else if(key>guess)
			printf("half of %d to %d -> you are too low",low,high);
		else
			printf("half of %d to %d -> you are too high",low,high);
	    if(key>mid)
			low=mid;
		else
			high=mid;	
	}
	return 0;
}
