def singularPlural(String1, String2):
    if String2.isnumeric():
        if(int(String2)==-1 or int(String2)==1):
            print(String1)
        else:
            if((String1[-1] in ('o','s','x','z')) or String1[-2:] == "ch" or String1[-2:] == "sh"):
                print(String1 + "es")
            elif(String1[-1] == 'y' and String1[-2] not in ('a','e','i','o','u')):
                print(String1[:-1:]+"ies")
            elif(String1[-2:] == "um"):
                print(String1[:-2:]+"a")
            else:
                print(String1 + "s")
    else:
        if String1 in String2:
            print("Singular : {}".format(String1))
            print("Plural : {}".format(String2))
        elif String2 in String1:
            print("Singular : {}".format(String2))
            print("Plural : {}".format(String1))
        else:
            print("Invalid Input")

def main():
    Str1 = input("Enter a word: ")
    Str2 = input("Enter a word or a number: ")
    singularPlural(Str1, Str2)

if __name__ == "__main__":
    main()
