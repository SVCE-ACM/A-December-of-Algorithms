# Dec 21
from csv import reader
d = dict()
with open('Dec21-Exchange_Rates.csv') as file:
    csv_reader = reader(file)
    for row in csv_reader:
        d[row[0].lower()] = row[1]

source = input('From Country: ').lower()
curr = float(input('Currency I have: '))
dest = input('To Country: ').lower()

rate = curr * (float(d[dest]) / float(d[source]))
print(f"{curr} ({source}) = {round(rate,2)} ({dest})")

# Sample I/O
# From Country: india
# Currency I have: 1000
# To Country: russia
# 1000.0 (india) = 895.55 (russia)
