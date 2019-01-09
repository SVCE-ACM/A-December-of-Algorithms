def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

a = str(input("Enter the string to be reversed: "))
print(reverse(a))
