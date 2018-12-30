# include <stdio.h>
void towerOfHanoi(int, char[], char[], char[]);
int main(void)
{
	int n;
	char Rod1[]="left", Rod2[]="middle", Rod3[]="right";
	printf("\nInput Number Of Disks : ");
	scanf("%d", &n);
	towerOfHanoi(n, Rod1, Rod3, Rod2);
  printf("\n");
	return 0;
}
void towerOfHanoi(int n, char Tower1[], char Tower3[], char Tower2[])
{
	if(n==1)
	 {
		printf("\n%s => %s", Tower1, Tower3);
		return ;
	 }
	towerOfHanoi(n-1, Tower1, Tower2, Tower3);
	printf("\n%s => %s", Tower1, Tower3);
	towerOfHanoi(n-1, Tower2, Tower3, Tower1);
}
