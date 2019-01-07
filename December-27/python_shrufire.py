def VowelSquare(a):
    for i in range(len(a) - 1):
        for l in range(len(a[i]) - 1):
            if a[i][l] in 'aeiou' and a[i][l+1] in 'aeiou' and a[i+1][l] in 'aeiou' and a[i+1][l+1] in 'aeiou':
                return str(i) + '-' + str(l)
    return 'not found'
s=input()
print(VowelSquare(s.split(',')))

