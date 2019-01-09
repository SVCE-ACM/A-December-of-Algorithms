// Java program to check if a URL is valid 
import java.net.URL; 

public class Test { 

	/* Returns true if url is valid */
	public static boolean isValid(String url) 
	{ 
		try { 
			new URL(url).toURI(); 
			return true; 
		}  
		catch (Exception e) { 
			return false; 
		} 
	} 
		
	public static void main(String[] args) 
	{ 
    Scanner s = new Scanner(System.in);
		String url = s.nextLine();
		if (isValid(url)) 
			System.out.println("Yes"); 
		else
			System.out.println("No");	 		 
	} 
} 
