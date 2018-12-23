/* Program which takes in a string and then prints distinct words with the number of times they appeared. */
using System;
using System.Collections.Generic;

class Sentence {

	private List<string> list;
	private string sentence;

	public Sentence(string sentence) {
		list = new List<String>();
		this.sentence = sentence;
	}

	public string[] GetDistinctWords() {

		string[] wordArray = sentence.Split(new char[] {' '});
		int length = wordArray.Length;

		for(int count = 0; count < length; count++ ){
			if(AlreadyExistsInList(wordArray[count])) { }
			else { list.Add(wordArray[count]); }
		}

		return list.ToArray();

	}

	private bool AlreadyExistsInList(string word) {
		foreach (string element in list){
			if(element==word) { return true; }
		}
		return false;
	}

}

public class Test {

	public static void Main() {

		Sentence s = new Sentence("My name is Arjun and name is not a thing it is a thing or name");
		string[] arr = s.GetDistinctWords();

		int length = arr.Length;
		
		for(int count=0; count < length; count++) {
			Console.Write("{0} ", arr[count]);
		}

	}

}
