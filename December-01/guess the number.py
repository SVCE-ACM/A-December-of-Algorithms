#Program for guessing the number

import os

clear_cmd = 'clear' if os.name =='posix' else 'cls'

os.system("clear")
print("--------------------------Welcome to guess the number------------------")

number = int(input("Player A enter a number between 0 to 100\n"))
os.system("clear")
print("Player B you have 7 tries to guess the correct number")

for chance in range(7):
    guess = int(input("chance: "+str(chance+1)+"  Enter your guessed number"))
    if(guess == number):
        print("Spot on!")
        print("Congratulations! you guessed the number in "+str(chance+1)+" chances")
        break
    elif(guess < number):
        print("That's too low!")
    else:
        print("That's too high!")
else:
    print("Sorry you have exceeded the maximum number of chances\nBetter luck next time!")
