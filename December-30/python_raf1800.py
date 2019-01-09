def di(n):
    diags = int(n * (n-3)/2)
    print("Number of diagonals: {}".format(diags))
    
def main():
    x=int(input("Enter number of sides: "))
    di(x)
    
if __name__ == "__main__":
    main()

