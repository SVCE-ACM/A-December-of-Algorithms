def strings(n):
    stringcount = int(n * (n-3)/2) + n
    print("Number of strings: {}".format(stringcount))
    
def main():
    x=int(input("Enter number of people: "))
    strings(x)
    
if __name__ == "__main__":
    main()

