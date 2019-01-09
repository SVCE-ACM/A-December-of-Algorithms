#include <iostream>
using namespace std;

int islucky(int nn){
    int no[100],count=0,s=0,r=0,i;

    for(i=0;nn>0;i++){
            no[i]=nn%10;

            nn=nn/10;
            count++;
    }


    for(i=0;i<count/2;i++){
        s+=no[i];
    }
     for(i=(count/2);i<count;i++){
        r+=no[i];
    }


    if(s==r){
        return 1;}

    return 0;
}


int main()
{
    int n;
    cout<<"Enter the number n: ";
    cin>>n;

    int lucky=islucky(n);
    if(lucky==1) cout<<"Lucky";
    else cout<<"unlucky";
}
