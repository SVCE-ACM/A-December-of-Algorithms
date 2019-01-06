def prefix(strings):
     plen = len(strings[0])
     for i in strings[1:]:
        plen = min(plen,len(i))
        while not i.startswith(strings[0][:plen]):
               plen=plen-1

     prefix=strings[0][:plen]
     if len(prefix)<2:
          print("No common prefix")
     else:
         print("Common prefix: ",prefix)

lis=input("Enter a list of strings(seperated by commas): ")
input_str=lis.lower().split(",")
print("Given input: ",input_str)
prefix(input_str)
