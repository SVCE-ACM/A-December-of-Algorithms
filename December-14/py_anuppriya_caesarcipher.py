def encrypt():
    string = input("Enter string: ")
    shift = int(input("Enter shift number: "))
    print("Original string: ", string)
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    print("After encryption: ",cipher)
encrypt()
