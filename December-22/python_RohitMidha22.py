def splitting_func(x):
    word=x.lower().split()
    return word
x=(input("Enter the string: "))
newlist=splitting_func(x)
dict = {}
for i in newlist:
    if i not in dict:
        dict[str(i)]=1
    else:
        dict[str(i)]+=1
print(dict)
