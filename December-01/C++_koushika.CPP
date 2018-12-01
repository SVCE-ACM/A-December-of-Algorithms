/*
Author: Koushika Kesavan
Date of Creation: 30 November 2018, Friday
Time Complexity: log(n)
All rights reserved
*/
#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void main()
{
clrscr();
int min=0,max=100,beg,end,mid;//Range set static, can be set dynamically too.
char str[40];
cout<<"\nRULES";
cout<<"\n1.You are PLAYER A,think of a secret number for PLAYER B to guess";
cout<<"\n2.PLAYER B is the computer.";
cout<<"\n3.Enter 'too high' if the PLAYER B's guessed number is greater than PLAYER A`s number";
cout<<"\n4.Enter 'too low' if the PLAYER B's guessed number is lower than PLAYER A`s number";
cout<<"\n5.Enter 'gotcha' if the number is found"<<"\n\n";
beg=min;
end=max;
while(beg<=end)//PLAYER B (Binary Search)
{
mid=(beg+end)/2;
cout<<"Guess--->"<<mid<<"\n";
gets(str);
if(strcmp(str,"gotcha")==0)
{
break;
}
else if(strcmp(str,"too high")==0)
{
end=mid-1;
}
else
{
beg=mid+1;
}
}
}
