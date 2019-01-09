# Dec 7
def IsApproximatelyEqual(a, b):
    b = round(b)
    a = round(a)
    return (a == b)


a, b = map(float, input("Enter the two numbers ").split())
print(IsApproximatelyEqual(a, b))

# SAMPLE I/O
# Enter the two numbers 3.0 2.5706
# True
