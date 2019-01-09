word = input("Enter word")
num = input("Enter num/Word")

def singular(word):
    if(isplural(word)):
        return word[:-1]
    else:
       return word

def plural(word):
    if(isplural(word)):
        return word
    else:
        return word+'s'

def isplural(word):
    if(word[-1] == 's'):
        return singular(word)

if(num.isdigit()):
    if(int(num)== 1 or int(num)== -1):
        print(singular(word))
    else:
        print(plural(word))
else:
    if(isplural(word)==num):
        print("Singular: ",num)
        print("Plural: ",word)
    elif(isplural(num)==word):
        print("Singular: ",word)
        print("Plural: ",num)
    else:
        print("Invalid Input")
