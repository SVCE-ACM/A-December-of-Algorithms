def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

def main():
    x=input("Enter a string: ")
    print(reverse(x))
    
if __name__ == "__main__":
    main()

