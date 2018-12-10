using System;
using System.Linq;
using System.Collections;
using System.Collections.Generic;

class Node {
	/* Fields */
        private string value;
        private Node next;
        private Node down;

        /*Constructors*/
        public Node () {
                value = "0";
                next = null;
                down = null;
        }

        public Node (Node node) {
                this.value = node.value;
                this.next = node.next;
                this.down = node.down;
        }

        /* Properties */
	public string Value {
		get { return value; }
		set { this.value = value; }
	}

        public Node Next {
                get { return next; }
		set { next = value; } 
        }

        public Node Down {
                get { return down; }
		set { down = value; }
        }
}


class LinkedList {

	/* Fields */
	private Node head;

	/* Constructors */
	public LinkedList () {
		head = null;
	}

	/* Functions */
	/* We first create all the public functions */
	public void AddNext (string value) {
		/* We add a node to the main linked list */
		Node pos = head;
		
		Node temp = new Node();
		temp.Value = value;

		while ( pos != null ) {
			/* We add the node at the end */
			if ( pos.Next == null ) {
				pos.Next = temp;
				break;
			}
			pos = pos.Next;
		}
	}

	public void AddChild (string value, int nodeNumber) {
		/* We add a child node to a main node */
		Node pos = GetMainNode(nodeNumber);
	
		/* We declare the new node */
		Node temp = new Node();
		temp.Value = value;

		while ( pos != null ) {
			/* We go down and add a child at the last position */
			if ( pos.Down == null ) {
				pos.Down = temp;
				break;
			}
			else if ( pos.Down.Value == value ) {
				/* If the value is already there, no adding it */
				break;
			}
			pos = pos.Down;
		}
	}

	public void PrintChildren (int nodeNumber) {
		/* Prints all the children of a specified main node */
		Node pos = GetMainNode(nodeNumber);

		Console.Write("All the children under Node %v are :-\n", nodeNumber);

		while ( pos != null ) {
			/* We print all the values of the children nodes */
			string value = pos.Down.Value;
			Console.Write("%v\n", value);

			pos = pos.Down;
		}

		Console.Write("\n");
	}

	public string[] GetChildrenArray (int nodeNumber) {
		/* Converts that particular main node's children into an array */
		int length = GetChildrenLength(nodeNumber);
		Node main = GetMainNode(nodeNumber);

		return GetArray(main, length);
	}

	
	/* The private functions are declared here */
	private int GetChildrenLength (int nodeNumber) {
		/* We get the length of a specified main node */
		Node pos = GetMainNode(nodeNumber);
		pos = pos.Down;

		int count;
		for ( count = 0; pos != null; pos = pos.Down ) {
			/* Increment count with every node */
			count++;
		}

		return count;
	}

	private Node GetMainNode (int nodeNumber) {
		/* We get the specified main node */
		Node pos = head;

		for ( int count = 0; count < nodeNumber; count++ ) {
			/* We get the position of the main node */
			pos = pos.Next;
		}

		return pos;
	}

	private string[] GetArray (Node main, int length) {
		/* We get all the elements and make them into an array */
		string[] array = new string[length];
		main = main.Down;		

		for ( int count = 0; count < length; count++ ) {
			array[count] = main.Value;
			main = main.Down;
		}

		return array;
	}
}



class HashTable {

	/* Fields */
	private LinkedList list;

	/* Constructors */
	public HashTable () {
		list = new LinkedList();
		for ( int iter = 0; iter < 9; iter++ ) {
			list.AddNext(iter.ToString());
		}
	}

	/* Public functions */
	public void HashItUp (string sentence) {
		string[] words = toArray(sentence);
		int length = words.Length;

		for ( int count = 0; count < length; count++ ) {
			/* Here, we apply th hash function to these words */
			int hash = HashFunction(words[count]);
			list.AddChild(words[count], hash);
		}
	}

	public void Display1 () {
		list.PrintChildren(1);
	}

	/* Private functions */
	private string[] toArray (string sentence) {
		var punctuation = sentence.Where(Char.IsPunctuation).Distinct().ToArray();
		var words = (sentence.Split().Select(x => x.Trim(punctuation))).ToArray();
		return words;
	}

	private int HashFunction (string value) {
		/* We add up the length of the string until it is less than 10 */
		int length = value.Length;
		int hashValue = GetLength(length);
		return hashValue;
	}

	private int GetLength (int length) {
		if ( length < 10 ) {
			return length;
		}
		else{
			int sum = 0;
			while ( length != 0 ){
				sum += (length%10);
				length /= 10;
			}
			return GetLength(sum);
		}
	}

}



public class Test {
	public static void Main(){
		//LinkedList list;

		HashTable h=new HashTable();
		h.HashItUp("My name is arjunaravind and my friend is Aravind Balakrishnan. He lives in Chennai in thiruvanmiyur and he is an awesom person. Recently he went to the UnitedStatesOfAmerica and he is on vacation there.");
		h.Display1();
	}
}
