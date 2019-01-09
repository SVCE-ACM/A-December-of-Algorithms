#getting a number from the user
n=int(input("Enter the nth number:"))
#function definition
def fibo(num):
    if num ==0:
        return 0
    elif num==1:
        return 1
    else:
        #calling recursively
        return fibo(num-1)+fibo(num-2)
#function call    
x=fibo(n)
#displaying the output
print("The",n,"th element is ",x)
