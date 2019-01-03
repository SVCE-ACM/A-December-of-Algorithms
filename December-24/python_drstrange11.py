# Dec 24
word = input('Enter string: ')
st = word


def rev(num):
    global st
    if num == 0:
        return st[0]
    else:
        return st[num]+rev(num-1)


print("Reversed String: ", rev(len(st)-1))

# SAMPLE I/O
# Enter string: string STRING
# Reversed String:  GNIRTS gnirts
