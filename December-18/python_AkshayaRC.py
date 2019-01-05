import re
import time
import itertools
file=open("pwd.txt","r")
pwd=input("enter password: ")
flag=0
start=time.time()
for i in file:
    z=re.search(pwd,i)
    if z:
     end=time.time()
     tt=end-start
     flag=1
     break
if flag==0:    
    ch=[]   
    for i in range(32,127):
      ch.append(chr(i))
    ##print(ch)
    for i in range(1,9):
      for j in itertools.product(ch,repeat=i):
        j=''.join(j)
        if j == pwd:
           end = time.time()
           tt=end-start
print("Time taken to bruteforce:",tt,"s")
