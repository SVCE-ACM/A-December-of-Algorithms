#include<stdio.h>
void main(){
int s1[3],s2[3],a1[3],a2[3],i,flag=0,flag1=0,flag2=0;
float r1,r2,r3;
printf("Enter the angles and side of the First triangle:\nNOTE FIRST INPUT ALL THE SIDES , THEN INPUT ALL  THEANGLES\n");
for(i=0;i<3;i++){
scanf("%d",&s1[i]);
}
for(i=0;i<3;i++){
scanf("%d",&a1[i]);
}
printf("Enter the angles and side of the Second triangle:\nNOTE FIRST INPUT ALL THE SIDES , THEN INPUT ALL  THEANGLES\n");
for(i=0;i<3;i++){
scanf("%d",&s2[i]);
}
for(i=0;i<3;i++){
scanf("%d",&a2[i]);
}
//checking the sides for sss congruence
if((s1[0]/s2[0])==(s1[1]/s2[1])==(s1[2]/s2[2])){
    flag=1;
}
else if((s1[0]/s2[0])==(s1[1]/s2[2])==(s1[2]/s2[1])){
    flag=1;
}
else if((s1[0]/s2[1])==(s1[1]/s2[0])==(s1[2]/s2[2])){
    flag=1;
}
else if((s1[0]/s2[1])==(s1[1]/s2[2])==(s1[2]/s2[0])){
    flag=1;
}
else if((s1[0]/s2[2])==(s1[1]/s2[1])==(s1[2]/s2[0])){
    flag=1;
}
else if((s1[0]/s2[2])==(s1[1]/s2[0])==(s1[2]/s2[1])){
    flag=1;
}

//checking for at least one equal angle for sas congruence

if(a1[0]==a2[0]||a1[1]==a2[1]||a1[2]==a2[2]){
    flag1=1;
}
else if(a1[0]==a2[0]||a1[1]==a2[2]||a1[2]==a2[1]){
    flag1=1;
}
else if(a1[0]==a2[1]||a1[1]==a2[2]||a1[2]==a2[0]){
    flag1=1;
}
else if(a1[0]==a2[1]||a1[1]==a2[0]||a1[2]==a2[2]){
    flag1=1;
}
else if(a1[0]==a2[2]||a1[1]==a2[1]||a1[2]==a2[0]){
    flag1=1;
}
else if(a1[0]==a2[2]||a1[1]==a2[0]||a1[2]==a2[1]){
    flag1=1;
}

// checking for aaa congruence
if(a1[0]==a2[0]&&a1[1]==a2[1]&&a1[2]==a2[2]){
    flag2=1;
}
else if(a1[0]==a2[0]&&a1[1]==a2[2]&&a1[2]==a2[1]){
    flag2=1;
}
else if(a1[0]==a2[1]&&a1[1]==a2[2]&&a1[2]==a2[0]){
    flag2=1;
}
else if(a1[0]==a2[1]&&a1[1]==a2[0]&&a1[2]==a2[2]){
    flag2=1;
}
else if(a1[0]==a2[2]&&a1[1]==a2[1]&&a1[2]==a2[0]){
    flag2=1;
}
else if(a1[0]==a2[2]&&a1[1]==a2[0]&&a1[2]==a2[1]){
    flag2=1;
}
//printing
if(flag==flag1==flag2){
    printf("\nThe triangles are similar by SSS, AAA and SAS congruence ");
}
else if(flag==flag1){
    printf("\nThe triangles are similar by SSS and SAS congruence ");
}
else if(flag==flag2){
    printf("\nThe triangles are similar by SSS and AAA congruence ");
}
else if(flag==1){
    printf("\nThe triangles are similar by SSS congruence ");
}
else if(flag2==1){
    printf("\nThe triangles are similar by AAA congruence ");
}
else
{
printf("\nThe triangles are NOT similar ");

}


}
