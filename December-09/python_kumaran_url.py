#python language
import validators
url=input("Enter the url:")
a=validators.url(url)
if a:
  print("TRUE")
else:
  print("FALSE") 
