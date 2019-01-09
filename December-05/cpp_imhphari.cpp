#include <iostream>
using namespace std;

void toh(int n,char a ,char c,char b){
    if(n==1){
        cout<<"Move disk 1 from "<<a<<" to "<<c<<"\n";
        return ;}
    else
        toh(n-1,a,b,c);
        cout<<"Move disk "<<n<<" from "<<a<<" to "<<c<< "\n";
        toh(n-1,b,c,a);

    }


int main()
{
    int n;char a,b,c;
    cout<<"Enter the number of disks in tower 1: ";
    cin>>n;
    toh(n, 'A', 'C', 'B');
    return 0;
}
