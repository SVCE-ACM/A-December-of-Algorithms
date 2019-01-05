# include<iostream>
using namespace std;
int main(){
    int i,n,k,c,j=0,mid=0,l,sum1=0,sum2=0,count1=1;
cout<<"Enter a number with even digits :";
cin>>n;
k=n;
l=n;
//checking for length of the number
while(l>1){
    count1++;
    l=l/10;
}
mid=count1/2;
i=1;
// checking for lucky number
while(n>=1){
    c=n%10;
    if(i<=mid){
        sum1=sum1+c;
        i++;
    }
    else{
        sum2=sum2+c;
    }
    n=n/10;
}
if(sum1==sum2){
    cout<<k<<" is a lucky number!";
}
else{
    cout<<k<<" is a NOT lucky number!";
}
return 0;
}
