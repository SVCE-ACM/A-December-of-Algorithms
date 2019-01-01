n=int(input("Enter the number of sides in the polygon:"))
if(n<3):
    print("Number of diagonals: 1")
else:
    print("Number of diagonals: ",int(n*(n-3)/2))
    
