def isAproximatelyEqual(a,b):
    if(round(a)==round(b)):
        print("isAproximatelyEqual("+str(a)+","+str(b)+") = true\n")
    else:
        print("isAproximatelyEqual("+str(a)+","+str(b)+") = false\n")


a = float(input("Enter 1st number : "))

b = float(input("Enter 1st number : "))

isAproximatelyEqual(a,b)