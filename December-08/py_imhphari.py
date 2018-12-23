from pattern.text.en import singularize,pluralize

def SingularPlural(word,num):
    if type(num) is int:
        if num==1 or num==-1:
            w=singularize(word)
        else:
            w=pluralize(word)
        print(w)
    elif type(num) is str:
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
    
