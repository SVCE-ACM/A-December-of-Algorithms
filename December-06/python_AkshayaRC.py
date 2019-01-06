def main():
    print("enter two numbers: ")
    n1=int(input())
    n2=int(input())
    gcdno=gcd(n1,n2)
    lcm=(n1*n2)//gcdno
    print("LCM is",lcm)

def gcd(n1,n2):
  if(n2==0):
    return n1
  else:
    return gcd(n2,n1%n2)

main()

