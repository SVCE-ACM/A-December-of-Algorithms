def diagonals(n):
    if n<=3:
        diag=0
    else:
      segments=n*(n-1)//2
      diag=segments-n
    return diag

n=int(input("enter n sides: "))
print("No.of diagonals:",diagonals(n))
