def CC(word,gap) :
    result=list()
    count=1
    i=0
    while(count<=len(word)):
        if(word[i].isupper()):
            result.append(chr((ord(word[i])+gap-65)%26+65))
        else:
            result.append(chr((ord(word[i])+gap-97)%26+97))
        count+=1
        i+=1
    print (''.join(result))
    
def main():
    x=input("Enter a word: ")
    gap = int(input("Enter a number: "))
    CC(x,gap);
    
if __name__ == "__main__":
    main()
