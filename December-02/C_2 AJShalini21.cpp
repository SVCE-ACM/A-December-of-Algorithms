#include<stdio.h>
int main()
{
	int i,j=0,k,s[2][3],a[2][3],d=0,b=0,c=0,temp;
	while(j<2)
    {
    	printf("side %d =",j+1);
	    for(i=0;i<3;i++)
	    scanf("%d",&s[j][i]);		
	    printf("angle %d =",j+1);
	    for(i=0;i<3;i++)
	    scanf("%d",&a[j][i]);	 
		for(i=0;i<2;i++)
	    {
	    	for(k=i+1;k<3;k++)
	    	{
	    		if(s[j][i]>s[j][k])
	    		{
	    			temp=s[j][i];
	    			s[j][i]=s[j][k];
	    			s[j][k]=temp;
				
	    			temp=a[j][i];
	    			a[j][i]=a[j][k];
	    			a[j][k]=temp;
				}
			}
		}
		j++;
    }
    if((s[1][0]/s[0][0])==(s[1][1]/s[0][1])&&(s[1][1]/s[0][1])==(s[1][2]/s[0][2]))
	d++;
    if(((s[1][0]/s[0][0])==(s[1][1]/s[0][1])||(s[1][1]/s[0][1])==(s[1][2]/s[0][2])||(s[1][2]/s[0][2])==(s[1][0]/s[0][0]))&&(a[1][0]==a[0][0]||a[1][1]==a[0][1]||a[1][2]==a[0][2]))
	b++;
	if((a[1][0]==a[0][0])&&(a[1][1]==a[0][1])&&(a[1][2]==a[0][2]))	
	c++;
	if(d==0&&b==0&&c==0)
	printf("THe triangles are not similar");
	else
	{
		printf("The triangles are similar by\t");
		if(d!=0)
        printf("SSS\t");
		if(b!=0)
		printf("SAS\t");
		if(c!=0)
		printf("AAA\t");		
	}
	return 0;
}
