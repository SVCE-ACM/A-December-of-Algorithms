import math

def LCM(*argv):
    args=argv[0]
    lcm=args[0]
    for i in args[1:]:
        lcm = int(lcm * i / math.gcd(lcm,i))
    print("LCM of the numbers: {}".format(lcm))
        


def main():
    a=[]
    n=int(input("Enter number of inputs: "))
    for i in range(0,n):
       a.append(int((input("Enter number {}: ".format(i+1)))))
    LCM(a)

if __name__ == "__main__":
    main()
