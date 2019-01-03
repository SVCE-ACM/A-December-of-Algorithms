# Dec 18
import time
import itertools

# ASCII 32-127
allowed = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_-+=[{]}|:;'\",<.>/?"


def bruteforce(p):
    global allowed
    start = time.time()
    for x in range(1, 9):
        for word in itertools.product(allowed, repeat=x):
            word = ''.join(word)
            if word == p:
                end = time.time()
                return round(end-start, 2)


s = input("Enter Password: ")
print(f"Maximum time taken to brute-force: {bruteforce(s)} seconds")

# SAMPLE I/O
# Enter Password: abc
# Maximum time taken to brute-force: 0.02 seconds
