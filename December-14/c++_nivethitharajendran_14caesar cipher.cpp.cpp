#include<iostream>
 
using namespace std;
 
int main()
{
    char str[100], ch;
    int i, key;
    
    cout << "Enter a string : ";
    cin>>str;
    cout << "Enter key: ";
    cin >> key;
    
    for(i = 0; str[i] != '\0'; ++i)
	{
        ch = str[i];
        
        if(ch >= 'a' && ch <= 'z')
		{
            ch = ch + key;
            
            if(ch > 'z')
			{
                ch = ch - 'z' + 'a' - 1;
            }
            
            str[i] = ch;
        }
        else if(ch >= 'A' && ch <= 'Z')
		{
            ch = ch + key;
            
            if(ch > 'Z'){
                ch = ch - 'Z' + 'A' - 1;
            }
            
            str[i] = ch;
        }
    }
    
    cout << "Encrypted String: " << str;
    
    



for(i = 0; str[i] != '\0'; ++i){
        ch = str[i];
        
        if(ch >= 'a' && ch <= 'z'){
            ch = ch - key;
            
            if(ch < 'a'){
                ch = ch + 'z' - 'a' + 1;
            }
            
            str[i] = ch;
        }
        else if(ch >= 'A' && ch <= 'Z'){
            ch = ch - key;
            
            if(ch > 'a'){
                ch = ch + 'Z' - 'A' + 1;
            }
            
            str[i] = ch;
        }
    }
        cout << "\nDecrypted message: " << str;
        return 0;
}
