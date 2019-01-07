#getting the string to be reversed from the user
a = str(input("Enter the string: "))
#function to reverse a string
def reverse(b):
    if len(b) == 0:
        return b
    else:
        #recursive call
        return reverse(b[1:]) + b[0]
#printing output
print(reverse(a))
