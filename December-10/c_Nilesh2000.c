#include<stdio.h>

void det_3x3(int arr[10][10],int m,int n)
{
    int i,det=0;
    for(i=0;i<3;i++)
        det+=(arr[0][i]*(arr[1][(i+1)%3]*arr[2][(i+2)%3] - arr[1][(i+2)%3]*arr[2][(i+1)%3]));
    printf("Determinant is : %d\n",det);

}
void det_2x2(int arr[10][10],int m,int n)
{
    //int det=0;
    int det;
    det = arr[0][0]*arr[1][1] - arr[1][0]*arr[0][1];
    printf("Determinant is : %d\n",det);
}
void main(){

    int arr[10][10],m,n;
    printf("Enter number of rows : "); scanf("%d",&m);
    printf("Enter number of columns : "); scanf("%d",&n);
    printf("Enter array : ");
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            scanf("%d",&arr[i][j]);
    if(m==3 && n==3)
        det_3x3(arr,m,n);
    else if(m==2 && n==2)
        det_2x2(arr,m,n);


}
