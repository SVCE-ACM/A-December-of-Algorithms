
#include <stdio.h> 


void spiralPrint(int m, int n, int a[10][10]) 
{ 
	int i, k = 0, l = 0; 

	while (k < m && l < n) 
	{ 
		/* Print the first row from the remaining rows */
		for (i = l; i < n; ++i) 
		{ 
			printf("%d ", a[k][i]); 
		} 
		k++; 

		/* Print the last column from the remaining columns */
		for (i = k; i < m; ++i) 
		{ 
			printf("%d ", a[i][n-1]); 
		} 
		n--; 

		/* Print the last row from the remaining rows */
		if ( k < m) 
		{ 
			for (i = n-1; i >= l; --i) 
			{ 
				printf("%d ", a[m-1][i]); 
			} 
			m--; 
		} 

		/* Print the first column from the remaining columns */
		if (l < n) 
		{ 
			for (i = m-1; i >= k; --i) 
			{ 
				printf("%d ", a[i][l]); 
			} 
			l++;	 
		}		 
	} 
} 

/* Driver program to test above functions */
int main() 
{ 
	int arr[10][10],m,n; 
    printf("Enter number of rows : "); scanf("%d",&m);
    printf("Enter number of columns : "); scanf("%d",&n);
    printf("Enter array : ");
    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
            scanf("%d",&arr[i][j]);

	spiralPrint(m,n, arr); 
	return 0; 
} 
