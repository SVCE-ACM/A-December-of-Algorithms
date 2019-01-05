def Fib(n):
    first = 0
    second = 1
    for i in range(0,n):
        print(first,end=" ")
        ne = first + second
        first = second
        second = ne



def main():
    n=int((input("Enter number of series elements: ")))
    Fib(n)

if __name__ == "__main__":
    main()
