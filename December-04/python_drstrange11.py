# Dec 4
def fib(n):
    f = list()
    f.append(0)
    f.append(1)
    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])
    return f[n - 1]


num = int(input("Enter the value of n "))
print(f"The number {num} in the Fibonacci Series is {fib(num)}")

# SAMPLE I/O
# Enter the value of n 5
# The number 5 in the Fibonacci Series is 3
