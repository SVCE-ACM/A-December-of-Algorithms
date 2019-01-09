#include<stdio.h>
int main()
{
	int a[5][5],m,n,i,j,k=0,c,v=0;
	printf("Enter the order(m*n) of the matrix ");
	scanf("%d%d",&m,&n);
	printf("Enter the matrix ");
	for(i=0;i<m;i++)
	for(j=0;j<n;j++)
	scanf("%d",&a[i][j]);
	i=0;
	c=m*n;
	while(k>=0)
    {
	for(j=k;j<n-k;j++)
	printf("%d ->\t",a[i][j]);
	v+=j;
	j--;
	if(v==c)
    break;
    else
	{
	for(i=k+1;i<m-k;i++)
	printf("%d ->\t",a[i][j]);
	v+=i;
	i--;
    }
	if(v==c)
	break;
	else
	{
	for(j=n-2-k;j>=0+k;j--)
	printf("%d ->\t",a[i][j]);
	j++;
	v+=j;
    }
	if(v==c)
	break;
	else
	{
	for(i=m-k-2;i>0+k;i--)
	printf("%d ->\t",a[i][j]);	
	i++;
	v+=i;
    }
    if(v==c)
    break;
    k++;
}
	return 0;
}
