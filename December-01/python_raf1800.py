import random
#For secret number
n=random.randint(0,100)

##To get secret number from User
#n = int(input("Enter the secret number: "))
 
low=0
high=100
check=True

while check:
    x=int((low+high)/2)
    if(x<n):
        print("Guess: {}. Secret Number is greater than this".format(x))
        low=x
    if(x>n):
        print("Guess: {}. Secret Number is lesser than this".format(x))
        high=x
    if(x==n):
        print("Guess: {}. That's the secret number!".format(x))
        check=False
