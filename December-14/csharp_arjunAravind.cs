using System;
using System.Text;

static class Cipher {

    public static StringBuilder Caesarize(string word, int value) {
        StringBuilder s = new StringBuilder(word.Length);
        int length = word.Length;
        
        for(int iter=0; iter<length; iter++) {
            s.Append((char)(word[iter]+value));
        }

        return s;
    }

}

public class CaesarCipher {
    public static void Main() {
        string word = Console.ReadLine();
        int val = Console.Read()-48;

        Console.Write("\nThe string is now --> {0}.\n",Cipher.Caesarize(word, val));
        Console.ReadKey();
    }
}
