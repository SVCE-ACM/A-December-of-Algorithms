#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
import inflect

def plural(words,num):
  if num>1 :
    p = inflect.engine()
    print([p.plural(word) for word in words.split(' ')])

  else:
      print(words)


def main():

    word=str(input("ENTER THE WORD:"))
    num=int(input("ENTER THE NUMBER 1->SINGULAR/2->PLURAL:"))
    plural(word,num)

if __name__ == '__main__':
    main()
