# Dec 22
# Change the text file if you want
with open('text.txt') as file:
    l = file.readlines()
word = []
for line in l:
    for x in line.split():
        word.append(x.lower())
word_distinct = set(word)
final = []
for word_1 in word_distinct:
    c = 0
    for words in word:
        if words == word_1:
            c += 1
    final.append((word_1, c))
for x, y in sorted(final):
    print(x, y)

# Sample I/O
# did 2
# martha! 1
# name? 2
# please! 1
# say 2
# stop! 1
# that 2
# why 2
# you 2
