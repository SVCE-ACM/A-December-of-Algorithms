# include <bits/stdc++.h>
using namespace std;
void readInput(int Arr[3])
{
  for(int i=0;i<3;i++)
   scanf("%d", &Arr[i]);
}
int similarAAA(int Angle1[], int Angle2[])
{
	sort(Angle1, Angle1 + 3);
	sort(Angle2, Angle2 + 3);
	 if(Angle1[0] == Angle2[0] && Angle1[1] == Angle2[1] && Angle1[2] == Angle2[2])
	  return 1;
	 else
	  return 0;
}
int similarSAS(int Side1[], int Side2[], int Angle1[], int Angle2[])
{
	sort(Angle1, Angle1 + 3);
	sort(Angle2, Angle2 + 3);
	sort(Side1, Side1 + 3);
	sort(Side2, Side2 + 3);
	if( Side1[0] / Side2[0] == Side1[1]/Side2[1])
	 {
		if(Angle1[2]==Angle2[2])
			return 1;
	 }
	if(Side1[1]/Side2[1] == Side1[2]/Side2[2])
	 {
		if(Angle1[0] == Angle2[0])
			return 1;
	 }
	if(Side1[2]/Side2[2] == Side1[0]/Side2[0])
	 {
		if(Angle1[1] == Angle2[1])
			return 1;
		}
	return 0;
}
int similarSSS(int Side1[], int Side2[])
{
	sort(Side1, Side1 + 3);
	sort(Side2, Side2 + 3);
	 if(Side1[0] / Side2[0] == Side1[1]/Side2[1] && Side1[1]/Side2[1] == Side1[2]/Side2[2])
	  return 1;
	return 0;
}
int main(void)
{
	int s1[3], s2[3], a1[3], a2[3];
  printf("Input:");
  printf("\nSide1 = ");
  readInput(s1);
  printf("Angle1 = ");
  readInput(a1);
  printf("Side2 = ");
  readInput(s2);
  printf("Angle2 = ");
  readInput(a2);
  printf("Output: ");
	int AAA = similarAAA(a1, a2);
	int SSS = similarSSS(s1, s2) ;
	int SAS = similarSAS(s1, s2, a1, a2) ;
	 if(AAA == 1 || SSS == 1 || SAS == 1)
	 {
		cout <<"Triangles are similar by ";
		 if(AAA == 1)
      cout <<"AAA ";
		 if(SSS == 1)
      cout <<"SSS ";
		 if(SAS == 1)
      cout <<"SAS";
	 }
	 else
		cout <<"Triangles are not similar.\n";
	return 0;
}
