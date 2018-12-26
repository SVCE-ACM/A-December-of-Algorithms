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
     printf("\nGuess %d (half of %d to %d) -> ", Arr[Mid], First, Last+1);
      if(Arr[Mid]==Search)
       {
         printf("spot on!");
         Flag=1;
          break;
       }
      else if(Arr[Mid]<Search)
       {
         printf("you're too low.");
         First=Mid+1;
       }
      else
       {
         printf("you're too high.");
         Last=Mid-1;
       }
    }
   if(Flag==0)
    printf("\nElement Not Found!!");
}
