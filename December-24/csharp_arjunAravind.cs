using System;
using System.Text;

public class Program{

	private StringBuilder sb;

	public Program() {
		sb = new StringBuilder("");
	}

	public void RecursiveReverse(string word, int index) {
		if (word.Length == 0) { return; }
		else if (index >= word.Length) { return; }
		else if (index >=0 && index < word.Length){
			RecursiveReverse(word,index+1);
			sb.Append(word[index]);	
		}	
	}

	public string Reverse(string word) {
		RecursiveReverse(word,0);
		return sb.ToString();
	}

	public static void Main() {

		Program p = new Program();

		string word = Console.ReadLine();

		Console.Write("'{0}' is the reverse of '{1}'.\n", p.Reverse(word), word);

	}

}
