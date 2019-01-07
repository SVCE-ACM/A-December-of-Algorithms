import validators as vd

def isUrl(Link):
   Res=vd.url(Link)

   if(Res==True):
       print("True")
   else:
       print("False")

Str=input("Enter The URL To Be Checked : ")
isUrl(Str)
