# include <stdio.h>
void main()
{
  int n, Search;
  printf("\nEnter The Number Of Integers You Want To Input...");
  scanf("%d", &n);
  int Arr[n];
  printf("\nEnter The Elements of The Array...");
   for(int i=0;i<n;i++)
    scanf("%d", &Arr[i]);
  printf("Enter The Element To Be Searched For...");
  scanf("%d", &Search);
  int Flag=0, First=0, Last=n-1, Mid;
   while(First<=Last)
    {
     Mid=(First+Last)/2;
     printf("\nGuess %d (half of 0 to %d)", Mid, Arr[n]);
      if(Arr[Mid]==Search)
       {
         printf("\nElement Found At Position...%d", Mid+1);
         Flag=1;
          break;
       }
      else if(Arr[Mid]<Search)
       {
         First=Mid+1;
       }
      else
       {
         Last=Mid-1;
       }
    }
   if(Flag==0)
    printf("\nElement Not Found!!");
}
