import re
def check(s):
  if(re.match('https?://(www\.)?(\w+)(\.\w+)',s)):
    return True
  else:
    return False

  
s=input("Enter the URL : ")
print(check(s))
