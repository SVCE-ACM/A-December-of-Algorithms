#include<stdio.h>
#include<conio.h>
#include<iostream.h>
int approx(float num1,float num2)
{
float diff=0.5;
num1=num1+diff;
num2=num2+diff;
num1=int(num1);
num2=int(num2);
if(num1==num2)
return 1;
else
return 0;
}
void main()
{
int n;
float num1,num2;
cout<<"\nEnter two numbers:";
cin>>num1>>num2;
n=approx(num1,num2);
if(n==1)
cout<<num1<<" and "<<num2<<" numbers are approximately equal";
else
cout<<num1<<" and "<<num2<<" numbers are approximately equal";
getch();
}



