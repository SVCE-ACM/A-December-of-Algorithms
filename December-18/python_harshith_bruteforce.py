import time
import string
start = time.time()
def brute(pass1):
    strr=" "
    list1=[]
    list2 = []
    list3=[]
    list4=[]
    k=0
    length=0
    for i in pass1:
        list1.append(i)


    for i in string.ascii_letters:
          list2.append(i)


    for i in string.digits:
          list3.append(i)


    for i in string.punctuation:
          list4.append(i)



    while strr!=pass1 :
       for j in list2:
           if list1[k]==j :
               strr+=" ".join(j)
               k+=1
               length+=1
               break
       if length>=len(list1) :
           break

       for j in list3:
           if list1[k]==j :
               strr+=" ".join(j)
               k+=1
               length+=1
               break
       if  length>=len(list1) :
           break

       for j in list4:
           if list1[k]==j :
               strr+=" ".join(j)
               k+=1
               length+=1
               break
       if length>=len(list1):
           break
    end = time.time()
    print("Time taken to brute_force is:",end-start)
password=input("ENTER THE PASSWORD:")
brute(password)
