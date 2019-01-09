from urllib2 import urlopen
import urllib2

def isURL(str):
    code = urlopen(str).code
    if (code/ 100 >= 4):
        return False
    if(code==200):
        return True

str = raw_input("Please enter URL : ")
if(isURL(str)):
    print("isURL("+str+")?  True \n")
else:
    print("isURL("+str+")?  False \n")
