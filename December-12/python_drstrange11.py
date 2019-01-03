# Dec 12
s = input("Enter the numbers with ->: ").split('->')
# Linked list is actually a list in python (No pointer concept in python)
s = [int(x) for x in s]
s.sort(reverse=True)
fin = ""
for x in s:
    fin = fin + f"{x} -> "
print(fin[:-3])

# Sample I/O
# Enter the numbers with ->: 10 -> 20 -> 34 -> 23 -> 889
# 889 -> 34 -> 23 -> 20 -> 10
