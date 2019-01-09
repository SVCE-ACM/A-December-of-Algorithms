using System;

class Permute {

	private char[] startRanges;
	private char[] endRanges;
	private int possibilities;

	public Permute() {
		/* We init the start/end ranges and number of possibilities */
		startRanges = new char[] {'A','a','0'};
		endRanges = new char[] {'Z','z','9'};

		possibilities = CalcPossibilityNumber(startRanges, endRanges) + 23;
	}

	public double GetPermutations(string password) {
		double length = password.Length;
		return Math.Pow((double)possibilities, length);
	}

	public double GetSeconds(double perm, double permPerSecond) => (perm/permPerSecond);

	private int CalcPossibilityNumber(char[] startRanges, char[] endRanges) {
		/* We return the total number of possibilities per character of password */
		int length = startRanges.Length;
		int sum = 0;

		for (int iter = 0; iter < length; iter++) {
			int range = endRanges[iter] - startRanges[iter];
			sum += range;
		}

		return sum;
	}

}

public class Program {

	public static void Main () {

		Console.Write("Enter the password --> ");
		string password = Console.ReadLine();
		Permute perm = new Permute();

		Console.Write("It takes {0} seconds.\n", perm.GetSeconds(perm.GetPermutations(password),500000));

	}

}
