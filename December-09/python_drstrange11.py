# Dec 9
import re


def IsURL(s):
    pattern = re.compile(r'https://\w+\.\w+')
    res = pattern.search(s)
    if res:
        return True
    else:
        return False


url = input("Enter URL ")
print(IsURL(url))

# SAMPLE I/O
# Enter URL https://duckduckgo.com
# True
