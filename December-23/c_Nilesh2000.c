# include <stdio.h>
void main()
{
  int roomNos, roomsize, deptNos;
  printf("\nNumber of classrooms: ");
  scanf("%d", &roomNos);
  printf("Size of classrooms(1-50): ");
  scanf("%d", &roomSize);
  printf("Enter the number of departments (2-10): ");
  scanf("%d", &deptNos);
  int stdDept[deptNos];
   for(i=0;i<deptNos;i++)
    {
      printf("Students in department %d (1-100):", i+1);
      scanf("%d", &stdDept[i]);
    }
}
