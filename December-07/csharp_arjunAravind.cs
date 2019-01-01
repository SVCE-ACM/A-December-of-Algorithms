using System;

public class Conversion {

	public static void Main () {
	
		Console.Write("Enter a first number --> ");
		float numberOne = Convert.ToSingle(Console.ReadLine());

		Console.Write("Enter a second number --> ");
                float numberTwo = Convert.ToSingle(Console.ReadLine());

		long number1 = (long)numberOne;
		long number2 = (long)numberTwo;

		if ( ( numberOne - (float)number1 ) < 0.5 ) {
			number1++;
		}
		if ( ( numberTwo - (float)number2 ) < 0.5 ) {
			number2++;
		}

		//This seperates these two statements

		if ( number1 == number2 ) {
			Console.Write("They are approximately equal!\n");
		}
		else {
			Console.Write("They are approximately not equal!\n");
		}

	}

}
