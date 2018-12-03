                        //  Similar Triangles
#include<stdio.h>
float t1_s[3],t2_s[3];
int t1_a[3],t2_a[3];
int i;
void triangle1()
{	printf("\n\n---------------------------------------------------------------");
	printf("\n\n\n\t\t\t\t\tEnter the sides of the triangle 1");
	for(i=0;i<3;i++)
	{
		printf("\nEnter the value of side %d:",i+1);
		scanf("%f",&t1_s[i]);
	}
	printf("\n\n\n\t\t\t\t\tEnter the Angles of the triangle 1");
	for(i=0;i<3;i++)
	{
		printf("\nEnter the value of angle %d:",i+1);
		scanf("%d",&t1_a[i]);
	}
	printf("\n\n---------------------------------------------------------------");
}
void triangle2()
{
	printf("\n\n---------------------------------------------------------------");
	printf("\n\n\n\t\t\t\t\tEnter the sides of the triangle 2");
	for(i=0;i<3;i++)
	{
		printf("\nEnter the value of side %d:",i+1);
		scanf("%f",&t2_s[i]);
	}
	printf("\n\n\n\t\t\t\t\tEnter the Angles of the triangle 2");
	for(i=0;i<3;i++)
	{
		printf("\nEnter the value of angle %d:",i+1);
		scanf("%d",&t2_a[i]);
	}
	printf("\n\n---------------------------------------------------------------");
}
void compare()
{
	printf("\n\n-----------------------------RESULTS----------------------------------");
float d=0,c,e,f,a=0,b=0;
	for(i=0;i<3;i++)
	{	
	if(t1_a[i]==t2_a[i] || t1_a[i]== t2_a[2-i])
	d++;	
}
c=t1_s[0]/t2_s[0];
e=t1_s[1]/t2_s[1];
f=t1_s[2]/t2_s[2];
if(c == e && e== f && f==c)
{
a++;
printf("\nThe given triangle is similar triangle By SSS");
}
if((t1_s[0]/t2_s[0] == t1_s[1]/t2_s[1]  && t1_a[1]==t2_a[1]) || (t1_s[1]/t2_s[1] == t1_s[2]/t2_s[2] && t1_a[2]==t2_a[2] ) || (t1_s[2]/t2_s[2] == t1_s[0]/t2_s[0] &&  t1_a[0]==t2_a[0]) )
{
	b++;	
printf("\n\nThe given triangle is similar triangle By SAS ");
}
if(d==3)
printf("\n\nThe given triangle is smilar triangle By AAA");
if(a==0 && b==0  && d!=3)
printf("\n\nThe triangles are not similar:");
printf("\n\n---------------------------------------------------------------");	
}
void main()
{
	int ch;
	do
	{	
	printf("\n1.Enter or change values of 1st triangle\n2.Enter or change values of 2nd triangle\n3.compare\n4.exit\n\n\t\tEnter your choice:");
	scanf("%d",&ch);	
	switch(ch)
	{
		case 1:
			{
				triangle1();
				break;
			}
		case 2:
		{
			triangle2();
			break;
			}
		case 3:
		{
			compare();
			break;
				}
			}
	}while(ch<=3);
}

