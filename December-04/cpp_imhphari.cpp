#include <iostream>
using namespace std;

int main()
{
    int f[100],i,n;
    f[0]=0;f[1]=1;


    cout<<"Enter the position to find in fibonacci sequence: ";
    cin>>n;
    for(i=2;i<n;i++){

        f[i]=f[i-1]+f[i-2];
    }
    cout<<"The "<<n<<"th element is "<<f[n-1];
}
