 # include <bits/stdc++.h>
using namespace std;
int findMinLength(string Str[], int n)
{
	int Min=Str[0].length();
	for(int i=1;i<n;i++)
		if(Str[i].length()<Min)
			Min=Str[i].length();
	return Min;
}
string commonPrefix(string Str[], int n)
{
	int minLen=findMinLength(Str, n);
	string Res;
	char Cur;
	 for(int i=0;i<minLen;i++)
	  {
		 Cur=Str[0][i];
		  for(int j=1;j<n;j++)
			 if(Str[j][i]!=Cur)
				return Res;
		 Res+=Cur;
	  }
	return Res;
}
int main()
{
  int numOfStrings;
  printf("\nHow Many Strings Would You Like To Enter: ");
  scanf("%d", &numOfStrings);
	string s[numOfStrings];
  printf("\nInput : ");
   for(int i=0;i<numOfStrings;i++)
    {
      cin >>s[i];
    }
	string Ans=commonPrefix(s, numOfStrings);
  printf("Output :");
	 if(Ans.length())
		cout <<" \"" <<Ans <<"\"\n";
	 else
		cout <<" \"No common prefix\"\n";
	return 0;
}
