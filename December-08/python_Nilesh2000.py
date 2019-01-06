def singularPlural(String1, String2):
    if String2.isnumeric():
        if(int(String2)==-1 or int(String2)==1):
            print(String1)
        else:
            if(String1[-1] == 's' or String1[-1] == 'x' or String1[-1] == 'z' ):
               #or String1.find("ch", len(String1)-3) or String1.find("sh", len(String1)-3)):
                print(String1 + "es")
            elif(String1[-1] == 'y'):
                print(String1[:-1:]+"ies")
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
