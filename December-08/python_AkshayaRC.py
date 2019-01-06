from pattern3.en import singularize,pluralize
def SingularPlural(word,num):

    try:
        num=int(num)
        if num==-1 or num==1:
            w=singularize(word)
        else:
            w=pluralize(word)
        print(w)

    except ValueError:
      if type(num) is str:
        if word==singularize(num):
            print("Singular: ",singularize(word))
            print("Plural: ",pluralize(word))
        elif num==singularize(word):
            print("Singular: ",singularize(num))
            print("Plural: ",pluralize(num))
        elif singularize(word)==singularize(num):
            print("Singular: ",word)
            print("Plural: ",pluralize(word))
        else:
            print("Invalid Input")
ans="yes"
while(ans=="yes"):
   word=input("Enter a noun: ")
   num=input("Enter an integer or string: ")
   SingularPlural(word,num)
   ans=input("continue? (yes/no) " )
