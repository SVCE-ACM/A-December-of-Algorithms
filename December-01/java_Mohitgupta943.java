import java.util.*;
public class dec1 {

	public static void main(String[] args) {
		
Scanner sc=new Scanner(System.in);
System.out.print("Enter the length of array:");
int len=sc.nextInt();
int []a=new int[len];
System.out.println("Enter elements of array:");
for(int i=0;i<len;i++)
{
	a[i]=sc.nextInt();
}
Arrays.sort(a);
System.out.println("Enter the element to find:");	
int n=sc.nextInt();
int x=binary_search(a,n,0,len-1);

if(x==-1)System.out.println("Element not found in array");
else System.out.println("Element found at index "+x+" in the array");
	}
	
	public static int binary_search(int[]a,int x,int si,int li)
	{
		int n=a.length;
		int st=si,lt=li;
		int mid=(((st+lt)/2));
		if(si>li)
			return -1;
		if(x==a[mid])
		{
			return mid;
		}
		else if(x>a[mid])
		{
			return binary_search(a,x,mid+1,n-1);
		}
		else if(x<a[mid])
		{
			return binary_search(a,x,0,mid-1);
		}
		
		return 0;
	}

}
