#include <stdio.h> 

void towerOfHanoi(int n, char from, char to, char extra) 
{ 
	if (n == 1) 
	{ 
		printf("\n Move disk 1 from rod %c to rod %c", from, to); 
		return; 
	} 
	towerOfHanoi(n-1, from, extra, to); 
	printf("\n Move disk %d from rod %c to rod %c", n, from, to); 
	towerOfHanoi(n-1, extra, to, from); 
} 

int main() 
{ 
	int n;
    printf("Enter number of disks, n: ");
    scanf("%d",&n);
    towerOfHanoi(n, 'L', 'R', 'M'); 
    printf("\n");
	return 0; 
} 
