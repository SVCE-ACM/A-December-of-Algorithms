import re
def IsURL(s):
    if(re.match(r'https://*\.com/*',s,re.M|re.I)):
        print("True")
    else:
        print("False")
    
def main():
    s = input("Enter a string: ")
    IsURL(s)
    
if __name__ == "__main__":
    main()
