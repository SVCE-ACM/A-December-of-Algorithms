#include<stdio.h>

int main()
{
    int side1[3];
    int side2[3];
    int angle1[3];
    int angle2[3];
    int sss=0;
    int sas=0;
    int aa=0;
    int c=0;
    printf("Side 1: ");
    for(int i=0;i<3;i++)
        scanf("%d",&side1[i]);
    printf("\nAngle 1: ");
     for(int i=0;i<3;i++)
        scanf("%d",&angle1[i]);
    printf("\nSide 2: ");
     for(int i=0;i<3;i++)
        scanf("%d",&side2[i]);
    printf("\nAngle 2: ");
     for(int i=0;i<3;i++)
        scanf("%d",&angle2[i]);

if(side1[0]/side2[0]==side1[1]/side2[1]&&side1[1]/side2[1]==side1[2]/side2[2])
{
    sss++;
}
if((side1[0]/side2[0]==side1[1]/side2[1]&&angle1[1]==angle2[1])||(side1[1]/side2[1]==side1[2]/side2[2]&&angle1[2]==angle2[2])||(side1[2]/side2[2]==side1[0]/side2[0]&&angle1[0]==angle2[0]))
{
    sas++;
}

if(angle1[1]==angle2[1]||angle1[1]==angle2[0]||angle1[1]==angle2[2])
{
    c++;
}
if(angle1[0]==angle2[0]||angle1[0]==angle2[1]||angle1[0]==angle2[2])
{
    c++;
}
if(angle1[2]==angle2[0]||angle1[2]==angle2[1]||angle1[2]==angle2[2])
{
    c++;
}
if(c>=2)
{
    aa++;
}
printf("Triangles are similar by: ");
if(sss>0)
{
    printf("SSS ");
}
if(aa>0)
{
    printf("AAA ");
}
if(sas>0)
{
    printf("SAS ");
}
    printf("\n");
    return 0;
}