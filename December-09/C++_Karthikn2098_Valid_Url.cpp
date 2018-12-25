/*
    This program works with the -std=c++11 or -std=gnu++11 compiler options.
*/

#include <iostream>
#include <regex>
using namespace std;

int main(void) {

    string Url_Regular_Expression = "(http|https)://([^/ :]+):?([^/ ]*)(/?[^ #?]*)\\x3f?([^ #]*)#?([^ ]*)";

    string URL = "https://duckduckgo.com/?q=test+string&atb=v143-2__&ia=web";

    if ( regex_match( URL , regex(Url_Regular_Expression) )) {
        cout << "\nValid URL.\n";
    }
    else {
        cout << "\nNot a Valid URL.\n";
    }

    return 0;
}

/*
Input0:
            URL = "https://duckduckgo.com/?q=test+string&atb=v143-2__&ia=web";
Output0:
            Valid URL.

Input1:
            URL = "Martha?";
Output1:
            Not a Valid URL.

*/
