using System;
using System.IO;

/* The objective of this program is to read from a csv file. */

public class CurrencyConvertor {

	static string ExtractCountry(string line) {
		
		string country="";

		for (int index = 0; true; index++ ) {
			if (line[index]==',') { break; }
			else { country += line[index]; }
		}

		return country;

	}

	static double ExtractCurrency(string line) {

		int startIndex = line.IndexOf(",");
		int length = line.Length;

		string currency="";

		for (int index = startIndex+1; index < length; index++) {
			currency += line[index];
		}

		return Convert.ToDouble(currency);

	}

	public static void Main() {
	
		string csvPath = @"../src/docs/Dec21-Exchange_Rates.csv";

		Console.Write("Enter the country whose currency you have --> ");
		string currentCurrency = Console.ReadLine();

		Console.Write("Enter the amount of money that you have --> ");
		long amountMoney = Int32.Parse(Console.ReadLine());

		Console.Write("Enter the country to which you want to convert it to --> ");
		string futureCurrency = Console.ReadLine(); 

		using (StreamReader sr = File.OpenText(csvPath)) {

			string line;

			double futureConversion=-1;
			double currentConversion=-1;

			while((line = sr.ReadLine()) != null){

				//5400 rs; 65/1*5400

				if (ExtractCountry(line) == futureCurrency) {
					futureConversion = ExtractCurrency(line);
				}
				if (ExtractCountry(line) == currentCurrency) {
					currentConversion = ExtractCurrency(line);
				}

				if (futureConversion != (-1) && currentConversion != (-1)) {
					double moneyAmount = (currentConversion/futureConversion) * amountMoney;
					Console.Write("The converted amount is {0}.\n", moneyAmount);
					break;
				}

			}

		}

	}

}
