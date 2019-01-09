def common_prefix(strings):

    if len(strings) == 1:
        return strings[0]

    prefix = strings[0]

    for string in strings[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:len(prefix)-1]
        if not prefix:
            break
    return prefix
       

string=list()
no=int(input("Enter the number of strings: "))
for i in range(0,no):
        n=input("Enter the string {}:".format(i+1))
        string.append(n)

print (common_prefix(string))
