def fib(n):
    a=0
    b=1
    if n==1:
        c=a
    elif n==2:
        c=b
    while (n-2)>0:
        c=a+b
        a=b
        b=c
        n=n-1
    return c
n=int(input('Enter the value of N(Nth term): '))
if n>3:
    print(n,'th term of the Fibonacci Series is ',fib(n))
elif n==3:
    print(n,'rd term of the Fibonacci Series is ',fib(n))
elif n==2:
    print(n,'nd term of the Fibonacci Series is ',fib(n))
elif n==1:
    print(n,'th term of the Fibonacci Series is ',fib(n))
else:
    print('Invalid Input')
