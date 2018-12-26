/*
Author: Koushika Kesavan
Date of Creation: 26 December 2018, Tuesday
Title: Fibonacci series
All rights reserved
*/

#include<stdio.h>
#include<conio.h>
#include<iostream.h>
#include<stdlib.h>
void main()
{
int i=0,n,first=-1,second=1,third;
cout<<"\nEnter the value of n:";
cin>>n;
while(i<n)
{
third=first+second;
first=second;
second=third;
i++;
}
cout<<"The nth value of a Fibonnaci series:"<<third;
getch();
}
