#include<stdio.h>
#include<conio.h>
#include<iostream.h>
void towers(int n, char frompeg, char topeg, char auxpeg)
{
if(n==1)
{
cout<<frompeg<<"-->"<<topeg<<"\n";
return;
}
towers(n-1,frompeg,auxpeg,topeg);
cout<<frompeg<<"-->"<<topeg<<"\n";
towers(n-1,auxpeg,topeg,frompeg);
}
void main()
{
clrscr();
int n;
cout<<"\nEnter number of disks:";
cin>>n;
towers(n,'A','C','B');//A-->LEFT,C-->RIGHT,B-->MIDDLE
getch();
}