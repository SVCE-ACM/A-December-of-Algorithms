def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
a=[]
for i in range(n):
    b=fibonacci(i)
    a.append(b)

print(a[-1])    
