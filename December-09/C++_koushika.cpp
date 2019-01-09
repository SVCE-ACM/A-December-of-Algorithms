#include <iostream>
#include<regex>

using namespace std;

void IsURL(std::string str,
        std::regex reg)
        {
    
     // This holds the first match
    std::sregex_iterator currentMatch(str.begin(),
            str.end(), reg);
    
    // Used to determine if there are any more matches
    std::sregex_iterator lastMatch;
    
    // While the current match doesn't equal the last
    while(currentMatch != lastMatch){
        std::smatch match = *currentMatch;
        std::cout << std::boolalpha;
        std::cout << "Checked for Results : " << 
                match.ready() << "\n";
        currentMatch++;
    }
    std::cout << "End\n";
       

}

int main()
{
    std::string str;
    std::cout << "Enter an example of URL: ";
    std::getline (std::cin,str);
    std::regex reg ("(https://[\\w]{2,20}\.[\\w]{1,3})");
    IsURL(str,reg);
    return 0;
}
