
#include <iostream>

using namespace std;

int main()

{

    int a=-1,b=1,c=0,n,i;
    cout<<"Enter n series";
    cin>>n;

    
  
  for(i=0;i<n;i++)
    {

        c=a+b;
  
      	cout<<"\n"<<c<<"\n";
 
       a=b;

        b=c;

    }

}

