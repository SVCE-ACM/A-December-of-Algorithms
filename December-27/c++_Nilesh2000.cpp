# include <iostream>
using namespace std;
bool isVowel(char Ch)
{
 Ch=tolower(Ch);
  switch(Ch)
   {
     case 'a':return true;
     case 'e':return true;
     case 'i':return true;
     case 'o':return true;
     case 'u':return true;
     default:return false;
   }
}
int main(void)
{
  int Flag=0, rowLength, colLength;
  cout <<"\nHow Many Rows And Columns In The Matrix :";
  cin >>rowLength>> colLength;
  char strArr[rowLength][colLength];
   for(int i=0;i<rowLength;i++)
    {
      for(int j=0;j<colLength;j++)
       {
         cin >>strArr[i][j];
       }
    }
   for(int i=0;i<rowLength;i++)
    {
      for(int j=0;j<colLength;j++)
       {
         if(isVowel(strArr[i][j]))
          {
            if(isVowel(strArr[i+1][j]))
             {
               if(isVowel(strArr[i][j+1]))
                {
                  if(isVowel(strArr[i+1][j+1]))
                   {
                     Flag=1;
                     printf("%d %d", i, j);
                      break;
                   }
                }
             }
          }
       }
    }
   if(Flag==0)
    cout <<"Not Found";
 return 0;
}
