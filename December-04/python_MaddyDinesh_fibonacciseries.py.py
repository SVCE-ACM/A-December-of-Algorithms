def fibo(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return(fibo(n-1)+fibo(n-2))
n=int(input("enter the nth number in fibonacci series"))
if n<1:
  print("enter a valid no")
else:
  print("fibonnaci of ",n,"th term is",fibo(n-1))
