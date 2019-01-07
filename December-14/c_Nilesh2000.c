# include <stdio.h>
void encryptKey(char [], int);
void decryptKey(char [], int);
int main(void)
{
  char Text[10];
  int Key;
  printf("\nInput: ");
  scanf("%s %d", Text, &Key);
  encryptKey(Text, Key);
  return 0;
}
void encryptKey(char Input[10], int k)
{
  int i;
   for(i=0;Input[i]!='\0';i++)
    {
      Input[i]+=k;
    }
  Input[i]='\0';
  printf("Encoded output: %s\n", Input);
}
void decryptKey(char Input[10], int k)
{
  int i;
   for(i=0;Input[i]!='\0';i++)
    {
      Input[i]-=k;
    }
  Input[i]='\0';
  printf("Decoded output: %s\n", Input);
}
