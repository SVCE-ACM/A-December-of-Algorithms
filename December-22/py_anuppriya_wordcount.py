import re
freq = {}
document_text = open('test.txt', 'r')
text = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{1,25}\b', text)
 
for word in match_pattern:
    count = freq.get(word,0)
    freq[word] = count + 1
     
freqlist = freq.keys()
 
for words in freqlist:
    print (words, freq[words])
