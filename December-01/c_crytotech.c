// C program to implement recursive Binary Search
#include <stdio.h>
//search begins
int binarySearch(int arr[], int l, int r, int x)
{
if (r >= l)
{
		int mid = l + (r - l)/2;


		if (arr[mid] == x){
			return mid;
		}

		if (arr[mid] > x)
			return binarySearch(arr, l, mid-1, x);

	
		return binarySearch(arr, mid+1, r, x);
}

// We reach here when element is not
// present in array
return -1;
}

int main(void)
{
int arr[100],i,n,x,m,ina,inb;
int result;
printf("Enter the number of elements you want in a array!\n");
scanf("%d",&n);
printf("Enter the array of numbers in a sorted manner\nPS: Binary search works only for a sorted list !!!\n");
for(i=0;i<n;i++){
  scanf("%d",&arr[i]);
}
printf("\nPlayer A choose a number: ");
scanf("%d",&x);
result = binarySearch(arr, 0, n-1, x);
if (result != -1){
ina=result;

//game starts
do{
printf("\nPlayer 2 start guessing the number: ");
scanf("%d",&m);
inb = binarySearch(arr, 0, n-1, m);
if(ina==inb)
    printf("Spot on");

else if(ina<inb)
    printf("Too high!");

else if(ina>inb)
    printf("Too low!");
}while(ina != inb);
}
else{
    printf("The number not found");
}
return 0;
}

