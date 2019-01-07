#include <iostream>
#include <map> // A map will be used to count the words.
#include <fstream> // Will be used to read from a file.
#include <string> // The map's key value.
using namespace std;


//Will be used to print the map later.
template <class KTy, class Ty>
void PrintMap(map<KTy, Ty> map)
{
    typedef std::map<KTy, Ty>::iterator iterator;
    for (iterator p = map.begin(); p != map.end(); p++)
        cout << p->first << ": " << p->second << endl;
}

int main(void)
{
    static const char* fileName = "C:\\MyFile.txt";

    // Will store the word and count.
    map<string, unsigned int> wordsCount;


    {
        // Begin reading from file:
        ifstream fileStream(fileName);

        // Check if we've opened the file (as we should have).
        if (fileStream.is_open())
            while (fileStream.good())
            {
                // Store the next word in the file in a local variable.
                string word;
                fileStream >> word;

                //Look if it's already there.
                if (wordsCount.find(word) == wordsCount.end()) // Then we've encountered the word for a first time.
                    wordsCount[word] = 1; // Initialize it to 1.
                else // Then we've already seen it before..
                    wordsCount[word]++; // Just increment it.
            }
        else  // We couldn't open the file. Report the error in the error stream.
        {
            cerr << "Couldn't open the file." << endl;
            return EXIT_FAILURE;
        }

        // Print the words map.
        PrintMap(wordsCount);
    }

    return EXIT_SUCCESS;
}
