#include <stdio.h>
int binarySearch(int a[], int beg, int end, int ele)
{
   if (end >= beg)
   {
        int mid =(end+beg)/2;

        if (a[mid] == ele)
            return mid;

        if (a[mid] > ele){
             printf("B:%d\nA:You're too high\n",a[mid]);
            return binarySearch(a, beg, mid-1, ele);}


        else{
        printf("B:%d\nA:You're too low\n",a[mid]);
        return binarySearch(a, mid+1, end, ele);}
   }

   return -1;
}

int main(void)
{
   int a[100],ele;
   for(int i=0;i<100;i++)
    a[i]=i+1;
   
   printf("A:Choose your secret number between 1 and 100:");
   scanf("%d",&ele);
   int n = sizeof(a)/ sizeof(a[0]);

   int x = binarySearch(a, 0, n-1, ele);
   if(x == -1)
   printf("Element is not present ")
   else
   printf("B:Your secret number is: %d\n",result+1);
   return 0;
}