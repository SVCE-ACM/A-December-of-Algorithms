import inflect

def plural(words,n):
  if n > 1 :
    p = inflect.engine()
    print([p.plural(word) for word in words.split(' ')])

  else:
      print(words)

word=str(input("Enter Word: :"))
num=int(input("Enter Choice : 1. Singular 2. Plural :"))
plural(word,num)
