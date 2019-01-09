def IsApprox(n1,n2,t):
    print (abs(n1 - n2) <= t)    

def main():
    n1 = float(input("Enter a number: "))
    n2 = float(input("Enter another number: "))
    t = float(input("Enter Tolerance level: "))
    IsApprox(n1,n2,t)

if __name__ == "__main__":
    main()
