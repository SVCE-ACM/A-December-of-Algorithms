def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list
wordstring = input('Enter the string: ')
words = wordstring.split()
wordlist=[]
for i in words:
    wordlist.append(i.lower())
wordlist.sort()
word=[]
for w in wordlist:
    x=[w,wordlist.count(w)]
    word.append(x)
for i in Remove(word):
    for x in range(0,len(i),2): 
        print(i[x],'',i[x+1])
