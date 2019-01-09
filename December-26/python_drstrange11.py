# Dec 26
# Enter the strings with spaces
prefixes = input("Enter the strings: ").split()
dummy = []
max_pref = 4  # Setting max prefix length as 4
for i in range(max_pref-1, 0, -1):
    for word in prefixes:
        dummy.append(word[:i+1])
    if len(set(dummy)) == 1:
        break
    else:
        dummy.clear()
if dummy:
    print(dummy[0])
else:
    print("No common prefix")

# Sample I/O
# Enter the strings: Element Elegant
# Ele
