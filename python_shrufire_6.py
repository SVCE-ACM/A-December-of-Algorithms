a=int(input('Enter the first number: '))
b=int(input('Enter the second number: '))
def gcd(n1,n2):
    if n2:
        return gcd(n2,n1%n2)
    else:
        return n1
lcm=int((a*b)/(gcd(a,b)))
print('The LCM is',lcm)
