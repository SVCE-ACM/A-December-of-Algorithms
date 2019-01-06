def crypt(text,key,ans):
    c=""
    for i in text:
      x=ord(i)
      if ans.lower()=="encrypt":
         x=x+key
      elif ans.lower()=="decrypt":
         x=x-key 
      c+=chr(x)
    print("Output:",c)

text=input("Text:")
key=int(input("Key (0-25):"))
ans=input("Encrypt/Decrypt?")
crypt(text,key,ans) 
