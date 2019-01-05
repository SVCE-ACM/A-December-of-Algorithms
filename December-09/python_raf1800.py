import re
def IsURL(s):
    url = re.compile(r"https://\w+\.\w+")
    if url.search(s):
        print("True")
    else:
        print("False")

def main():
    s = input("Enter a string: ")
    IsURL(s)
    
if __name__ == "__main__":
    main()
