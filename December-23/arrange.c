#include<stdio.h>

	int nc,sc,nd;
	 
	char d[10][5];
	
	int ns[10];
	
	int t,r=0,c=0;
	
	char l[50][8];




void main()
{
	int i;
	printf("Enter the no.of class room:");
	scanf("%d",&nc);
	printf("\nSize of classrooms (1-50):");
	scanf("%d",&sc);
	printf("\nEnter the number of departments (2-10):");
	scanf("%d",&nd);
	
	for(i=0;i<nd;i++)
	{
		printf("\nDepartment %d Code:",i+1);
		 scanf(" %[^\n]",d[i]);
		printf("\nStudents in department %d (1-100):",i+1);
		scanf("%d",&ns[i]);
		r=r+ns[i];
	}
	
	t=nc*sc;
	
	printf("r=%d t=%d",r,t);
	int j=0
	const int b=0;
	
	while(c<t)
	{
	
	
	for(i=0;i<nc;i++)
	{
	
	
		while(c<ns[i])
		{
		
		printf("\n class room %d",i+1);    //sc //ns
		if(j%2==0)
		{
		
		l[j]=d[b];
		c++;
		j++;
		}
		else
		{
	
		l[j]=d[b+1];
		j++;
		c++;
		}
		
		
	}
	
}
	
}
