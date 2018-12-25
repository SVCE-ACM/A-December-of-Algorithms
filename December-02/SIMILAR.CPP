#include<stdio.h>
#include<conio.h>
#include<iostream.h>
#include<stdlib.h>
#include<iomanip.h>
int compare(const void* a, const void* b)
{
return(*(int*)a - *(int*)b);
}
int sss_sim(int* s1, int* s2)
{
qsort(s1,3,sizeof(int),compare);
qsort(s2,3,sizeof(int),compare);
if((s1[0]/s2[0]==s1[1]/s2[1])&&(s1[1]/s2[1]==s1[2]/s2[2])&&(s1[2]/s2[2]==s1[0]/s2[0]))
return 1;
else
return 0;
}
int aaa_sim(int* a1,int* a2)
{
qsort(a1,3,sizeof(int),compare);
qsort(a2,3,sizeof(int),compare);
if(a1[0]==a2[0] && a1[1]==a2[1] && a1[2]==a2[2])
return 1;
else
return 0;
}
int sas_sim(int* s1, int* s2, int* a1, int* a2)
{
qsort(s1,3,sizeof(int),compare);
qsort(s2,3,sizeof(int),compare);
qsort(a1,3,sizeof(int),compare);
qsort(a2,3,sizeof(int),compare);
if((s1[0]/s2[0]==s1[1]/s2[1]) && (a1[2]==a2[2]))
return 1;
else if((s1[1]/s2[1]==s1[2]/s2[2]) && (a1[0]==a2[0]))
return 1;
else if((s1[2]/s2[2]==s1[0]/s2[0]) && (a1[1]==a2[1]))
return 1;
else
return 0;
}
void main()
{
int s1[3],s2[3],a1[3],a2[3],i,sss,aaa,sas;
cout<<"Enter three sides of the 1st triangle";
cin>>s1[0]>>s1[1]>>s1[2];
cout<<"\nEnter three sides of the 2nd triangle";
cin>>s2[0]>>s2[1]>>s2[2];
cout<<"\nEnter three angles of 1st triangle";
cin>>a1[0]>>a1[1]>>a1[2];
cout<<"\nEnter three angles of 2nd triangle";
cin>>a2[0]>>a2[1]>>a2[2];
sss=sss_sim(s1,s2);
aaa=aaa_sim(a1,a2);
sas=sas_sim(s1,s2,a1,a2);
if((sss||aaa||sas)==1)
{
if((sss==1)&&(aaa==1)&&(sas==1))
cout<<"The triangles are similar by SSS,SAS,AAA property";
else if((aaa==1)&&(sss==1))
cout<<"The triangles are similar by AAA,SSS property";
else if((sas==1)&&(aaa==1))
cout<<"The triangles are similar by SAS,AAA property";
else if((sss==1)&&(sas==1))
cout<<"The triangles are similar by SSS,SAS property";
else if(sss==1)
cout<<"The triangles are similar by SSS property";
else if(sas==1)
cout<<"The triangles are similar by SAS property";
else
cout<<"The triangles are similar by AAA property";
}
else
cout<<"The triangles are not similar";
getch();
}



