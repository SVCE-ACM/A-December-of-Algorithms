def Hash(x):
    val=0
    hashed = list()
    for i in range(len(x)):
        val += ord(x[i])
    for i in range(7,12):
        hashed.append(val%i)
    print("".join(str(x) for x in hashed))
    
def main():
    x = input("Enter string: ")
    Hash(x)
    
if __name__ == "__main__":
    main()
