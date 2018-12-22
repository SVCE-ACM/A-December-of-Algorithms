#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
def caesar(string1,key):
    list1=[]
    strr=" "
    dict1={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    dict2 = { 1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g" ,8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",
             14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",
             26:"z"}
    for ltr in string1.lower():
        num=dict1[ltr]+key
        list1.append(dict2[num])
        strr="".join(list1)
    print(strr.upper())

def main():
    str1=str(input("ENTER THE STRING:"))
    num=int(input("ENTER THE KEY:"))
    caesar(str1,num)
if __name__ == '__main__':
    main()
