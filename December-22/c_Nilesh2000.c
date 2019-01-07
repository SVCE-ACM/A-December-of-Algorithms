# include <stdio.h>
# include <string.h>
int main()
{
  char Str[100], Words[100][100], Temp[100];
  int i, j, k, n, Count;
  j=k=0;
  //Accepting input
  gets(Str);
  //Copying Each and every word into a 2-D Array from the string
   for(i=0;Str[i]!='\0';i++)
    {
     if(Str[i]==' ')
      {
       Words[j][k]='\0';
       k=0;
       j++;
      }
     else
      {
       Words[j][k++]=Str[i];
      }
    }
  Words[j][k] = '\0'; //Null character for last word
  n=j+1; //Storing count of words
  //Sorting the array of words
  for(i=0;i<n-1;i++)
   {
    for(j=i+1;j<n;j++)
     {
      if(strcmp(Words[i], Words[j])>0)
       {
         strcpy(Temp, Words[i]);
         strcpy(Words[i], Words[j]);
         strcpy(Words[j], Temp);
       }
     }
   }
  printf("\n");
  //Displaying frequecncy of each word

   for(i=0;i<n;i+=Count) //Incrementing by count to process the next word
    {
     Count=1;
       {
        for(j=i+1;j<=n;j++)
          {
           if(strcmp(Words[i], Words[j])==0)
            {
             Count++;
            }
          }
       }
      printf("%s\t%d\n", Words[i], Count); //Count is used to display the frequecncy of each word
    }
  printf("\n");
  return 0;
}

//Source
//https://stackoverflow.com/questions/53970726/frequency-of-a-word-in-a-string/53971534#53971534
