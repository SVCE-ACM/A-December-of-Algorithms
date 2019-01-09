import re

file = open('dict.txt', 'r')
pas=input("Enter password:")
"""pas=r'^(pas)$'"""
pas= r"\b(?=\w)" + re.escape(pas) + r"\b(?!\w)"

from datetime import datetime
start_time = datetime.now()

for line in file.readlines():
    if re.search(pas, line, re.I):
        print (line)

end_time = datetime.now()
print('Maximum time taken to brute-force: {}'.format(end_time - start_time)+' seconds')
