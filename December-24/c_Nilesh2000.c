# include <stdio.h>
void reverseString(char *Str)
{
  if(*Str)
   {
     reverseString(Str+1);
     printf("%c", *Str);
   }
}
int main(void)
{
  char Str[100];
  printf("\nEnter String: ");
  gets(Str);
  printf("Reversed String: ");
  reverseString(Str);
  printf("\n");
  return 0;
}
