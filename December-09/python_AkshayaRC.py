import re
def IsURL(url):
    match=re.search(r'^http|https://.*$',url)
    mat=re.search(r'.com',url)
    if match and mat:
        print("true")
    else:
        print("false")
url=input("Enter url: ")
IsURL(url)
