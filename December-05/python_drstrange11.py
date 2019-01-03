# Dec 5
def Hanoi(n, l='left', r='right', m='middle'):
    if n == 1:
        print(f"{l} => {r}")
        return
    Hanoi(n-1, l, m, r)
    print(f"{l} => {r}")
    Hanoi(n-1, m, r, l)


num = int(input("Number of disks "))
Hanoi(num)

# SAMPLE I/O
# Number of disks 3
# left => right
# left => middle
# right => middle
# left => right
# middle => left
# middle => right
# left => right
