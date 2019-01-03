/* Get an array of strings and print the common prefix  */
using System;

public class Program {

	public string[] GetStrings() {

		Console.Write("How many strings would you like to enter --> ");
		int num = Int32.Parse(Console.ReadLine());

		string[] arr = new string[num];

		for(int index = 0; index < num; index++) {
			arr[index] = Console.ReadLine();
		}

		return arr;

	}

	public int FindCommonPrefix(string[] arr, int index) {

		if(arr.Length == 0) { return -1; }
		else{
			char letter = arr[0][index];
			for(int count = 1;  count < arr.Length; count++) {

				if(index >= arr[count].Length) { return index; }

				if(letter==arr[count][index]) { }
				else { return index; }
			}
		}
	
		return FindCommonPrefix(arr, index + 1);

	}

	public static void Main() {
		
		Program p = new Program();

		string[] arr = p.GetStrings();
		int prefix = p.FindCommonPrefix(arr,0);

		if(prefix==0) {
			Console.Write("There is no common prefix.\n");
		}
		else{
			Console.Write("'{0}' is the common prefix.\n", arr[0].Substring(0,prefix));
		}

	}

}
