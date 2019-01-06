#include <iostream>
#include <string>
using namespace std;

int main ()
{
	string str,str2,st;
	int n=0;
	char ch,ch2;
	cout<<"Enter a quantity of a noun and the enter the noun : \n";
    cin>>st;
	
  //IF A NUMBER IS GIVEN

	if(!(st=="1"||st=="-1"))
	{
		cin>>str;
		n=str.length();
		ch=str[n-1];
		ch2=str[n-2];

		if (ch=='y')
			str2=str.substr(0,n-1)+"ies";
		else if (ch=='o'||ch=='s'||ch=='x')
			str2=str+"es";
		else if (ch=='h'&& ch2=='c')
			str2=str+"es";
		else if (ch== 'f')
			str2=str.substr(0,n-1)+"ves";
		else if (ch=='e'&&ch2=='f')
			str2=str.substr(0,n-2)+"ves";
		else
			str2=str+"s";

		cout<<str<<"\t\t\t"<<str2<<endl;
	}
	else{
        cin>>str;
		n=str.length();
	str2=str;
	cout<<str<<"\t\t\t"<<str2<<endl;
	}
  
  // IF A STRING IS GIVEN 
  
    cout<<"\nEnter a noun or a string :\n";
    cin>>str;
		n=str.length();
		ch=str[n-1];
		ch2=str[n-2];

		if (ch=='y')
			str2=str.substr(0,n-1)+"ies";
		else if (ch=='o'||ch=='s'||ch=='x')
			str2=str+"es";
		else if (ch=='h'&& ch2=='c')
			str2=str+"es";
		else if (ch== 'f')
			str2=str.substr(0,n-1)+"ves";
		else if (ch=='e'&&ch2=='f')
			str2=str.substr(0,n-2)+"ves";
		else
			str2=str+"s";

		cout<<"singular : "<<str<<"\t\t"<<"plural : "<<str2<<endl;

	return 0;
}
