def Hanoi(n,lt,rt,mt):
    if n >= 1:
        Hanoi(n-1,lt,mt,rt)
        print(lt + " => " + rt)
        Hanoi(n-1,mt,rt,lt)
        


def main():
    n=int((input("Enter number of disks in left tower: ")))
    Hanoi(n,"Left","Right","Middle")

if __name__ == "__main__":
    main()
