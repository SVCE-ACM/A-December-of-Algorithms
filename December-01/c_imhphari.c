
#include <stdio.h>
int binarySearch(int arr[], int l, int r, int no)
{
   if (r >= l)
   {
        int mid = l + (r - l)/2;

        if (arr[mid] == no)
            return mid;

        if (arr[mid] > no){
             printf("B:%d\nA:You're too high\n",arr[mid]);
            return binarySearch(arr, l, mid-1, no);}


        else{
        printf("B:%d\nA:You're too low\n",arr[mid]);
        return binarySearch(arr, mid+1, r, no);}
   }

   return -1;
}

int main(void)
{
   int arr[100],no;
   for(int i=0;i<100;i++){
    arr[i]=i+1;
   }
   printf("A:Choose your secret number between 1 and 100:");
   scanf("%d",&no);
   int n = sizeof(arr)/ sizeof(arr[0]);

   int result = binarySearch(arr, 0, n-1, no);
   (result == -1)?  printf("Element is not present ")
                 : printf("B:Your secret number is: %d",
                                                   result+1);
   return 0;
}
