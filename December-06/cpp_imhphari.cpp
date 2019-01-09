#include <iostream>
using namespace std;

int gcd(int a,int b){
    if(b==0)
        return a;
    return gcd(b,a%b);
}

 int lcm(int arr[],int n)
{
    int result=arr[0];
    for (int i=1;i<n;i++)
        result=(((arr[i]*result))/(gcd(arr[i],result)));

    return result;
}
int main()
{
    int i,n;
    cout<<"Enter the number of elements :";
    cin>>n;
    int arr[n];
    for(i=0;i<n;i++){
        cin>>arr[i];
    }
    int no=sizeof(arr)/sizeof(arr[0]);
    int s=lcm(arr,no);
    cout<<s;
    return 0;

}
