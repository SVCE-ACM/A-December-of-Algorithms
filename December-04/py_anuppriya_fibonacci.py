def fib(n):
  if(n==1):
    return 0
  elif(n==2):
    return 1
  else:
    return(fib(n-1) + fib(n-2))





n=int(input("Enter the n'th number in Fibonacci Sequence: "))
result=fib(n)
print("The",n," th number in the series is",result)
