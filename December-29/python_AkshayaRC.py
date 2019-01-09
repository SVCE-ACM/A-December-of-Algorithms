def number(n):
       seg=n*(n-1)//2
       return seg

num=int(input("enter number of friends"))
print("Number of strings required:",number(num))
