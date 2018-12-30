from itertools import permutations 
def LexiArr(x) :
    letters = x
    perm = permutations(letters)
    poss = list(perm)
    poss.sort()
    j=1
    for i in poss:
        word=''.join(i)
        if(word==x):
            print (word + "  ---->   Match found here at position {}".format(j))
        else:
            print(word)
        j+=1

def main():
    x=input("Enter a word: ")
    LexiArr(x)
    
if __name__ == "__main__":
    main()
