# include <stdio.h>
int isLucky(int);
int main(void)
{
  int ticketNum;
  printf("\nEnter A Ticket Number...");
  scanf("%d", &ticketNum);
  int Res=isLucky(ticketNum);
   if(Res==1)
    printf("true");
   else
    printf("false");
  return 0;
}
int isLucky(int Num)
{
  int firstHalf=0, lastHalf=0, Digits=0;
  int tempNum=Num;
   while(tempNum!=0)
    {
      Digits++;
      tempNum/=10;
    }
    for(int i=(Digits/2)+1;i<=Digits;i++)
     {
       firstHalf+=(Num%10);
       Num/=10;
     }
   for(int i=1;i<=Digits/2;i++)
    {
      lastHalf+=(Num%10);
      Num/=10;
    }
   if(firstHalf==lastHalf)
    return 1;
   else
    return 0;
}
