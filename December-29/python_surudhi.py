n=int(input('Enter the number of people'))
if n<2:
    print('Cannot communicate')
else:
    print('Number of strings required: ',int((n*(n-1))/2))
