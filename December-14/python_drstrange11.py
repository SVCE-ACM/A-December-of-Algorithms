# Dec 14
st, num = input('Input: ').split()
st = list(st)
num = int(num)
for i in range(len(st)):
    st[i] = chr(ord(st[i]) + num)
encrypted = ''.join(x for x in st)
print('Encoded output:', encrypted)

# Decryption (Optional)
# def decrypt(s,num):
#     s = list(s)
#     for i in range(len(s)):
#         st[i] = chr(ord(st[i]) - num)
#     print('Decrypted:',''.join(x for x in st))

# decrypt(encrypted,num)

# Sample I/O
# Input: feel 4
# Encoded output: jiip
