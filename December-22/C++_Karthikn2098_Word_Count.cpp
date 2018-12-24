/*
Problem:

    Write a program that reads a string from a user into a text file
                    and prints out how often each word appears in the string.

      word1 count1
      word2 count2

*/

#include <bits/stdc++.h>
using namespace std;

/**
 * @desc: function to insert the word and it's count in a Hash map.
 * @param: address of the map , and the word to be inserted.
 */
void Insert(map<string, int> &map1, string word)
{
    //if the word already exists, incrementing the count of the word occurrences.
    if(map1.find(word) != map1.end())
        map1[word]++;
    //if the word doesn't exist already...
    else
        map1.insert( pair<string,int>(word,1) );
}


//main function...
int main(void) {

    fstream file;

    string word;

    vector<string> words;  //1D array of strings that stores every word from the file.

    map <string , int> word_count_map;     //HashMap which contains the word and it's respective count.

    file.open("D22_Word_Count.txt");

    while( file >> word ) {

        words.push_back(word);              //adding the word in a list(for sorting purpose).

        Insert(word_count_map , word);      //inserting the word in a map.

    }

    sort( words.begin() , words.end() );    //sorting the vector of strings...

    words.erase( unique(words.begin() , words.end()) , words.end() );   //removing duplicates from the vector of strings...

    //printing the word and its count
    for(vector<string>::iterator i = words.begin() ; i != words.end() ; ++i ) {
        cout << *i << " --->  " <<  word_count_map.find(*i) -> second << endl << endl;
    }

    return 0;
}

/*
Output:

Martha! --->  1

Please! --->  1

Stop! --->  1

Why --->  2

did --->  2

name? --->  2

say --->  2

that --->  2

you --->  2

*/
