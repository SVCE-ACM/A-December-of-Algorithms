#include <iostream>
#include <algorithm>
using namespace std;

int prop(int a1[], int a2[])
{
	sort(a1,a1+3);
	sort(a2,a2+3);

	if(a1[0]==a2[0] && a1[1]==a2[1] && a1[2]==a2[2])
        return 1;
	else
        return 0;

}
int sideangle(int s1[], int s2[],int a1[],int a2[])
{
	sort(a1,a1+3);
	sort(a2,a2+3);
	sort(s1,s1+3);
	sort(s2,s2+3);
	if( s1[0]/s2[0]==s1[1]/s2[1]){
		if (a1[2]==a2[2])
			return 1;}
	if (s1[1]/s2[1]==s1[2]/s2[2]){
		if(a1[0]==a2[0])
			return 1;}
	if(s1[2]/s2[2]==s1[0]/s2[0]){
		if(a1[1]==a2[1])
			return 1;}
	return 0;
}

int sides(int s1[],int s2[])
{
	sort(s1,s1+3);
	sort(s2,s2+3);

	if(s1[0]/s2[0] == s1[1]/s2[1] && s1[1]/s2[1]==s1[2]/s2[2]&& s1[2]/s2[2]==s1[0]/s2[0])
		return 1;

	return 0;
}

int main()
{
	int s1[3],s2[3],a1[3],a2[3],i;
	cout<<"Side 1:";
	for(i=0;i<3;i++){
        cin>>s1[i];
	}
	cout<<"Angle 1:";
	for(i=0;i<3;i++){
        cin>>a1[i];
	}
	cout<<"Side 2:";
	for(i=0;i<3;i++){
        cin>>s2[i];
	}
	cout<<"Angle 2:";
	for(i=0;i<3;i++){
        cin>>a2[i];
	}
	int aaa=prop(a1,a2);
	int sss=sides(s1,s2);
	int sas=sideangle(s1,s2,a1,a2);
	if(aaa==1||sss==1||sas==1)
	{
		cout<<"Triangles are similar by ";
		if(aaa==1)
            cout<<"AAA ";
		if(sss==1)
            cout<<"SSS ";
		if(sas==1)
            cout<<"SAS";
	}
	else
		cout<<"Triangles are not similar";
	return 0;
}

