import inflect
p = inflect.engine()
a=input("input 1 :")
b=input("input 2 :")
if b.isdigit():
    if b not in ['-1','1']:
        if a[-1]!="s":
            print(p.plural(a))
        else :
            print (a)
    else :
        if a[-1]== "s" :
            print(a[:-1])
        else :
            print(a)
else :
    if a[1:3]== b[1:3] :
        if a[-1]== "s" :
            e = p.plural(a)
            print ("singular :",e)
            print ("plural :",a)
        else :
            f = p.plural(a)
            print ("singular :",a)
            print ("plural :",f)
    else :
        print ("invalid input")
