#include<stdio.h>
#include<conio.h>
int sss (float side1[4] , float side2[4] )
{
 if(((side1[0]/side2[0])==(side1[1]/side2[1]))&&((side1[0]/side2[0])==(side1[2]/side2[2]))&&((side1[1]/side2[1])==(side1[2]/side2[2])))

   return 1;
 else
   return 0;
}
int aaa (int angle1[3] , int angle2[3])
{  if (((angle1[0]==angle2[0])&&(angle1[1]==angle2[1])&&(angle1[2]&&angle2[2]))||((angle1[0]==angle2[2])&&(angle1[1]==angle2[1])&&(angle1[2]==angle2[0])))	
     return 1;
   else 
     return 0 ;	 	
}
int sas (float side1[4], float side2[4], int angle1[4], int angle2[4])
{
	if (((side1[0]/side2[0])==(side1[1]/side2[1]))&& (angle1[1]==angle2[1]))
	 return 1;
	else if (((side1[0]/side2[0])==(side1[2]/side2[2]))&&(angle1[2]==angle2[2])) 
	return 1;
	else if (((side1[1]/side2[1])==(side1[2]/side2[2]))&&(angle1[0]==angle2[0])) 
	return 1;
	else
	return 0;
}
void main ()
{
	float side1[4],side2[4];
	int angle1[4],angle2[4],c,d,e,i,f;
do
{
		printf("enter the sides of 1st triangle");
	for(i=0;i<3;i++)
	 scanf("%f",&side1[i]);
	printf("enter the angles of 1st triangle");
    for(i=0;i<3;i++)
	 scanf("%d",&angle1[i]);
    printf("enter the sides of 2nd triangle");
	for(i=0;i<3;i++)
	 scanf("%f",&side2[i]);
    printf("enter the angles of 2nd triangle");
	for(i=0;i<3;i++)
	 scanf("%d",&angle2[i]);
	c= sss(side1,side2);
    d= aaa(angle1,angle2);
    e= sas(side1,side2,angle1,angle2);
	if((c==1)&&(d==1)&&(e==1))
	 printf("triangles are similar by sss aaa sas") ;
	else if ((c==1)&&(d==1))
	  printf("triangles are similar by sss aaa ");
	else if ((c==1)&&(e==1))
	  printf("triangles are similar by sss sas ");
	else if ((d==1)&&(e==1))
	  printf("triangles are similar by aaa sas ");
	else if (c==1)
	  printf("triangle is similar by sss");
	else if (d==1)
	  printf ("triangle is similar by aaa");
	else if (e==1)
	  printf("triangle is similar by sas");
	else 
	  printf("triangles are not similar");
	printf(" \n enter 1 to continue and 0 to stop");
	scanf("%d",&f)  ;
}while(f==1);
}


