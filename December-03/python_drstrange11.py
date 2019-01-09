# Dec 3
def isLucky(num):
    list_num = [int(x) for x in num]
    s = 0
    # Also takes the mid for odd number of numbers (not mentioned)
    for i in range(len(list_num) // 2):
        s += list_num[i]
    if s == sum(list_num) - s:
        return True
    return False


n = input("Enter a Number ")
print(isLucky(n))

# SAMPLE I/O
# Enter a Number 1230
# True
