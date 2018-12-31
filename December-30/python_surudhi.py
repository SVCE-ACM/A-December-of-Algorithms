n=int(input('Enter the number of sides of the polygon'))
if n<4:  
    print('Diagonals do not exist')
else:
    print('Number of diagonals are: ',int((n*(n-3))/2))
