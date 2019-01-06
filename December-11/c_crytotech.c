

#include <stdio.h>

void spiralPrint(int m, int n, int a[10][10])
{
	int i, k = 0, l = 0;

	while (k < m && l < n)
	{
		
		for (i = l; i < n; ++i)
		{
			printf("%d ", a[k][i]);
		}
		k++;

	
		for (i = k; i < m; ++i)
		{
			printf("%d ", a[i][n-1]);
		}
		n--;

		if ( k < m)
		{
			for (i = n-1; i >= l; --i)
			{
				printf("%d ", a[m-1][i]);
			}
			m--;
		}

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

// Enter the matrix
int main()
{
	/*int a[R][C] = { {1, 2, 3, 4, 5, 6},
		{7, 8, 9, 10, 11, 12},
		{13, 14, 15, 16, 17, 18}
	}; */
	int m,n,i=0,j=0;
	int a[10][10];
	printf("Enter the row and column of the matrix : ");
	scanf("%d%d",&m,&n);
    for(i=0;i<m;i++){
        for(j=0;j<n;j++){
            scanf("%d",&a[i][j]);
        }
        j=0;
    }
	spiralPrint(m, n, a);
	return 0;
}
