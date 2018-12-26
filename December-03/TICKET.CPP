#include<stdio.h>
#include<iostream.h>
#include<stdlib.h>
#include<conio.h>
void main()
{
long int n,i,count=0,temp1,a[100],sum1=0,sum2=0,temp2;
cout<<"\nEnter the ticket number:";
cin>>n;
temp1=n;
while(temp1)
{
a[count]=temp1%10;
temp1/=10;
count++;
}
temp2=count;
for(i=0;i<count/2;i++)
{
sum1+=a[i];
sum2+=a[temp2-1];
temp2--;
}
if(sum1==sum2)
{
cout<<"\nThe ticket number "<<n<<" is a lucky number";
}
else
{
cout<<"\nThe ticket number "<<n<<" is not a lucky number";
}
getch();
}