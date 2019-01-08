file = open("woord.txt",'r')
lines = file.readlines()

wordlist = []
countlist = []

for line in lines:
    words = line.split()
    for word in words:
        word = word.strip(".,!?:;'\"")
        word = word.lower()

        if word not in wordlist:
            wordlist.append(word)

        countlist.append(word)


wordlist.sort()
for word in wordlist:
    print(word, countlist.count(word))
