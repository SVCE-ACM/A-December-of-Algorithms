import time
import itertools
Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_.")
Password = input("Enter password: ")
start = time.time()
counter = 1
CharLength = 1

for CharLength in range(25):
    passwords = (itertools.product(Alphabet, repeat = CharLength))
    for i in passwords:
        counter += 1
        i = str(i)
        i = i.replace("[", "")
        i = i.replace("]", "")
        i = i.replace("'", "")
        i = i.replace(" ", "")
        i = i.replace(",", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        if i == Password:
            end = time.time()
            timetaken = end - start
            print('Maximum time taken to brute-force:',timetaken,'seconds')
