def IsApproximate(num1,num2):
    if round(num1)==round(num2):
        print("true")
    else:
        print("false")
def IsApproximatelyEqual(num1,num2,t):
    if abs(num1-num2)>t:
        print("false")
    else:
        print("true")
print("Enter two numbers")
num1=float(input())
num2=float(input())
ans=input("With tolerance level? (yes/no)")
if ans=="no":
    IsApproximate(num1,num2)
if ans=="yes":
    t=float(input("tolerance level:"))
    IsApproximatelyEqual(num1,num2,t)
