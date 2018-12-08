#include<stdio.h>
#include<string.h>

void spnum()
{
	char s1[20];
	int n,l,i;
	printf("\nEnter the string:");
	scanf("%s",s1);
	l=strlen(s1);
	//printf("\nlength=%d",l);
	printf("\nEnter 1 Or -1 to get singular form\nEnter 2 to get  plural form\n\n\t\t\t\t op= ");
	scanf("%d",&n);
	if(n==1 || n==-1)
	{
		//printf("\n came to 1st if");
		//printf("\ny=%c",s1[l-1]);
		if( s1[l-2]=='e' && s1[l-1]=='s'&& s1[l-3]=='i')
		{
			//printf("\n welcome");
			printf("SingularPlural(%s, %d)",s1,n);
			for(i=0;i<l-3;i++)
	        printf("%c",s1[i]);
	        printf("%c",'y');
		}
		else if(s1[l-1]=='s' && s1[l-2]=='e') 
		{
			printf("SingularPlural(%s, %d)",s1,n);
			for(i=0;i<l-2;i++)
			
			printf("%c",s1[i]);
			//s1[i+1]='\0';		
	
}
else if(s1[l-1]=='s')
{
	printf("SingularPlural(%s, %d)\n",s1,n);
	for(i=0;i<l-1;i++)
	printf("%c",s1[i]);
	
}
else if( s1[l-2]=='s' &&  s1[l-1]=='y' && (s1[l-3]== 'a' || s1[l-3]== 'e'|| s1[l-3]== 'i' || s1[l-3]=='o' || s1[l-3]=='u') )
{
	printf("SingularPlural(%s, %d)",s1,n);
	for(i=0;i<=l-1;i++)
	printf("%c",s1[i]);

}
	
		else
		{
		printf("SingularPlural(%s, %d)",s1,n);
		printf("\n %s",s1);}
}
else if(n==2)
{
	if(s1[l-1]=='s' || (s1[l-1]=='s' && s1[l-2]=='s' ) || (s1[l-1]=='h' && s1[l-2]=='s' ) || (s1[l-1]=='h' && s1[l-2]=='c' ) || s1[l-1]=='x' || s1[l-1]=='z'|| s1[l-1]=='o')
	{
			printf("SingularPlural(%s, %d)\n",s1,n);
	printf("%s",s1);
	printf("%s","es");
	
	}
	else if( s1[l-1]=='f')  
	{
		printf("SingularPlural(%s, %d)\n",s1,n);
		for(i=0;i<l-1;i++)
		printf("%c",s1[i]);
		printf("%s","ves");
	}
	else if  (s1[l-1]=='e' || s1[l-2]=='f')
	{
		printf("SingularPlural(%s, %d)\n",s1,n);
		for(i=0;i<l-2;i++)
		printf("%c",s1[i]);
		printf("%s","ves");
		
	}

   else if(  s1[l-1]=='y' && (s1[l-2]== 'a' || s1[l-2]== 'e'|| s1[l-2]== 'i' || s1[l-2]=='o' || s1[l-2]=='u') ) 
   {
   	printf("SingularPlural(%s, %d)\n",s1,n);
		for(i=0;i<=l-1;i++)
		printf("%c",s1[i]);
		printf("%c",'s');
   	
   }
   	else if(s1[l-1]=='y')
	{
		printf("SingularPlural(%s, %d)\n",s1,n);
		for(i=0;i<=l-2;i++)
		printf("%c",s1[i]);
		printf("%s","ies");
		
		
	}
		else if(s1[l-1]=='o')
	{
		printf("SingularPlural(%s, %d)\n",s1,n);
		for(i=0;i<=l-1;i++)
		printf("%c",s1[i]);
		printf("%s","es");
		
		
	}
	else
	{
			printf("SingularPlural(%s, %d)\n",s1,n);
			printf("%s%c",s1,'s');
		
	}
   
	
}

}

void spcheck()
{
	char s1[20],s2[20];
	int l1,l2;
	printf("\nEnter the 1st string:");
	scanf("%s",&s1);
	printf("\nEnter the 2nd string:");
	scanf("%s",&s2);
	l1=strlen(s1);
	l2=strlen(s2);
	
//	printf("%s",s1[0-3]);

if( l1>l2 && s1[0]==s2[0] && s1[1]==s2[1]  )
{
	printf("\nsingular=%s",s2);
	printf("\npulral=%s",s1);
}
else if( l2>l1 && s1[0]==s2[0] && s1[1]==s2[1]  )
{
	printf("\nsingular=%s",s1);
	printf("\npulral=%s",s2);
}
	
}



void main()
{
	int ch;
	do{
		printf("\n\n\n1.singular to pulral or pular to singular\n2.check string is pulral or singular \n3.exit\nEnter your choice:");
		scanf("%d",&ch);
		
		switch(ch)
		{
			case 1:
				{
					spnum();
					break;
				}
			case 2:
			{
				spcheck();
				break;
				}	
		}
	}while(ch<=2);

   
}
