import csv
def Conv(c1,c2,amt):
    change = 0
    count = 0
    c1i = 0
    c2i = 0
    currencies=list()
    countries=list()
    with open('Dec21-Exchange_Rates.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            x = " ".join(row)
            countries.append(x.split(',')[0])
            currencies.append(x.split(',')[1])
        countries.pop(0)
        currencies.pop(0)
    for i in countries:
        if(c1==i):
            c1i=count
        if(c2==i):
            c2i=count
        count+=1
    change = float(amt/float(currencies[c1i]))
    change = float(change*float(currencies[c2i]))
    print("Converted amount: {}".format(change))
            
            
def main():
    x = input("From Country: ")
    y = input("To Country: ")
    z = int(input("Amount: "))
    Conv(x,y,z)
    
if __name__ == "__main__":
    main()

