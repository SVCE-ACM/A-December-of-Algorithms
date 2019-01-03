using System;

/**
 * The objective of this program is to produce all possible combos
 * of a given word. We need a recursive program and a linked list.
 */

class Node {
    public char Value;
    public Node Next;

    public Node() => Next = null;
}

class LinkedList {
    Node head;

    public LinkedList() => head = new Node();

    public LinkedList(string word) {
        head = new Node();
        foreach (char letter in word)
            Add(letter);
    }

    public void Add(char value) {
        Node temp = new Node();
        temp.Value = value;

        for (Node pos = head; pos != null; pos = pos.Next) {
            if (pos.Next == null) {
                pos.Next = temp;
                break;
            }
        }

    }

    public void Remove(char value) {

        for (Node pos = head; pos != null; pos = pos.Next) {
            if(pos.Next.Value == value) {
                Node temp = pos.Next;
                pos.Next = pos.Next.Next;
                temp = null;
                break;
            }
        }

    }

    public int Length() {
        int count = 0;
        for (Node pos = head.Next; pos != null; pos = pos.Next, count++) ;
        return count;
    }
    
    public char this[int index] {
        get {
            int count = 0;
            for (Node pos = head.Next; pos != null; pos = pos.Next, count++) {
                if (count == index)
                    return pos.Value;
            }
            return '?';
        }
    }

    public void Print() {
        Console.Write("(");

        for (Node pos = head.Next;  pos != null; pos = pos.Next) {
            Console.Write("{0}, ", pos.Value);
        }

        Console.Write("\b\b)\n");
    }

    public void PrintWord() {
        for (Node pos = head.Next; pos != null; pos = pos.Next)
            Console.Write("{0}", pos.Value);
        Console.Write("\n");
    }
}

class Permutations {
    string Word;

    public Permutations(string word) {
        LinkedList usedLetters = new LinkedList();
        this.Word = word;
        RecursiveSolve(usedLetters);
    }

    public bool PresentInWord(char letter, LinkedList usedLetters) {
        int length = usedLetters.Length();
        for(int iter=0; iter<length; iter++) {
            if (letter == usedLetters[iter])
                return true;
        }
        return false;
    }

    public LinkedList GenerateList(LinkedList usedLetters) {
        LinkedList genList = new LinkedList();
        foreach(char letter in Word) {
            if (PresentInWord(letter, usedLetters))
                usedLetters.Remove(letter);
            else
                genList.Add(letter);
        }
        return genList;
    }

    public void RecursiveSolve(LinkedList usedLetters) {
        LinkedList genList = GenerateList(usedLetters);
        int length = genList.Length();

        for(int iter=0; iter<length; iter++) {
            usedLetters.Add(genList[iter]);

            if (length == 1) usedLetters.PrintWord();
            else RecursiveSolve(usedLetters);
        }

    }
}

class Program {
    public static void Main() {
        string word = Console.ReadLine();
        Permutations permute = new Permutations(word);
        Console.ReadKey();
    }
}
