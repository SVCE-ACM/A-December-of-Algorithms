# Dec 19
h = [0]*26


def hash_string(s):
    global h
    s = s.lower()
    val = ord(s[0])-97
    if h[val]:
        h[val].append(s)  # Separate chaining
    else:
        h[val] = [s]


h = [0]*26
hash_string("abc")
hash_string("car")
hash_string("zebra")
val = hash_string("apple")
print(h)  # prints hash table

# Sample I/O
# [['abc', 'apple'], 0, ['car'], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#  0, 0, 0, 0, 0, ['zebra']]
