def SingularPlural(s1,s2):
    if s2.isnumeric():
        if(int(s2)==-1 or int(s2)==1):
            print(s1)
        else:
            if(s1[-1] == 's' or s1[-1] == 'x' or s1[-1] == 'z'):
                print(s1 + "es")
            elif(s1[-1] == 'y'):
                print(s1[:le-1]+"ies")
            else:
                print(s1 + "s")
    else:
        if s1 in s2:
            if len(s1) > len(s2):
                print("Singular : {}".format(s2))
                print("Plural : {}".format(s1))
            else:             
                print("Singular : {}".format(s1))
                print("Plural : {}".format(s2))
        elif s2 in s1:
            if len(s1) > len(s2):
                print("Singular : {}".format(s2))
                print("Plural : {}".format(s1))
            else:             
                print("Singular : {}".format(s1))
                print("Plural : {}".format(s2))
        else:
            print("Invalid Input")
        
        
        

def main():
    s1 = input("Enter a word: ")
    s2 = input("Enter a string or another number: ")
    SingularPlural(s1,s2)

if __name__ == "__main__":
    main()
