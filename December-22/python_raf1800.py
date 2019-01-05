def counter():
    file = open("testfile.txt", "r") 
    words = file.readlines()
    words = words[0].split(' ')
    words.sort()
    count = {i : 0 for i in words}
    for i in words:
        for j in count.keys():
            if(j==i):
                count.update({j : count.get(j)+1})
    for key in count.keys():
        print ("{} : {}".format(key,count.get(key)))
    file.close()

def main():
    file = open("testfile.txt","w")
    x=input("Enter a string: ")
    file.write(x)
    file.close()
    counter()
    
if __name__ == "__main__":
    main()

