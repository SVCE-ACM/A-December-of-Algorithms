#include<stdio.h>
int main()
{
	int key,i=0,j;
	char arr[20],caes[20];
	printf("Plaintext: ");
	gets(arr);
	printf("Enter the key: ");
	scanf("%d",&key);
	j=(i+key)%26;
	while(arr[i]!='\0')
	{
		if(arr[i]==' ')
		caes[i]=arr[i];
		else
		caes[i]=arr[i]+j;
		i++;
	}
	caes[i]='\0';
	printf("\nEncoded Output = ");
	puts(caes);
	return 0;
}
