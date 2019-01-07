
import validators
url=input("ENTER THE INPUT")
a=validators.url(url)
if a:
  print("TRUE")
else:
  print("FALSE")  
