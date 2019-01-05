import java.util.*;
import java.io.*;
import java.lang.*;
public class approximatelyEqual{
    public static void main(String [] args){
    System.out.println("Enter two numbers : ");
    Scanner s = new Scanner(System.in);
    float a= s.nextFloat();
    float b= s.nextFloat();
    float tolerancePercentage= s.nextFloat();
    float diff = Math.abs(a - b);         
    float tolerance = tolerancePercentage/100 * a;  
    if(diff < tolerance){
    System.out.println("They are approximately equal!");
    }
    else{
    System.out.println("They are NOT approximately equal!");
    }
    }
}
