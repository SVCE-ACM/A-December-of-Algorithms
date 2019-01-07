import random
x=random.randint(1,100)
flag=1
u=1
l=100
while flag:
    g=int(input('Enter your guess: '))
    if x==g:
        flag=0
        print('Your guess is right,',x)
    else:
        if x>g:
            print('Your guess is lesser')
            u=g
            print('Guess a number between',u,' and ',l)    
        else:
            print('Your guess is more')
            l=g
            print('Guess a number between',u,' and ',l)
            
         


