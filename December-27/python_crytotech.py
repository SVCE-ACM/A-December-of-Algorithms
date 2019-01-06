def VowelSquare(a):
    for i in range(len(a)):
        for l in range(len(a[i])):
            if a[i][l] in 'aeiou' and a[i][l+1] in 'aeiou' and a[i+1][l] in 'aeiou' and a[i+1][l+1] in 'aeiou':
                return 'Top left Position of vowel square:' + str(i) + '-' + str(l)
    return 'Unavailable'
lis=input("Enter 2Dmatrix (seperated by commas )")
c=lis.split(",")
print(c)
print("The Matrix should be: ")
for i in c:
    for j in range(len(i)):
         print(i[j],end="  ")
    print(sep="\n")       
print(VowelSquare(c))
