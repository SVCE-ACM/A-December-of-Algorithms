# include <iostream>
# include <string>
using namespace std;
void encryptString(string s, int k)
{
  k%=26;
   for(int i=0;s[i]!='\0';i++)
   {
       int c=s[i];
        if(islower(c))
         {
          c+=k;
           if(c>'z')
               c=96+(c%122);
         }
        else if(isupper(c))
         {
          c+=k;
           if(c>'Z')
               c=64+(c%90);

         }
       cout <<(char)c;
   }
}
int main(void)
{
    int Key;
    string Text;
    cout <<"\nInput: ";
    cin >>Text >>Key;
    cout <<"Encoded output: ";
    encryptString(Text, Key);
    return 0;
}
